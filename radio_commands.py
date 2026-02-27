import subprocess
import sys

RADIO_URL = "https://livestream/playlist.m3u8" # fake token, por privacidad

radio_process = None


def play_radio():
    global radio_process

    if radio_process and radio_process.poll() is None:
        return f"Radio ya iniciada\n(PID: {radio_process.pid})"

    try:
        radio_process = subprocess.Popen(
            [
                "ffplay",
                "-nodisp",
                "-loglevel", "quiet",
                RADIO_URL
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True  # evita procesos huerfanos
        )

        return f"Radio iniciada\n(PID: {radio_process.pid})"

    except FileNotFoundError:
        return "Error: ffplay no está instalado o no está en el PATH."
    except Exception as e:
        return f"Error al iniciar la radio: {str(e)}"


def stop_radio():
    global radio_process

    if radio_process and radio_process.poll() is None:
        try:
            radio_process.terminate()
            radio_process.wait(timeout=3)

        except subprocess.TimeoutExpired:
            radio_process.kill()

        except Exception as e:
            return f"Error al detener la radio: {str(e)}"

        finally:
            radio_process = None

        return "Radio detenida correctamente."

    radio_process = None
    return "La radio no está en ejecución."