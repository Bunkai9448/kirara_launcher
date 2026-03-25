#!/bin/bash

CONFIG_FILE="~/ovpn-main/Country/IPconnection.ovpn"

PID_FILE="/tmp/openvpn.pid"

start_vpn() {
    if [ -f "$PID_FILE" ]; then
        echo "VPN is already running."
        exit 1
    fi

    echo "Starting OpenVPN..."
    sudo openvpn --config "$CONFIG_FILE" --daemon --writepid "$PID_FILE"

    sleep 2

    if [ -f "$PID_FILE" ]; then
        echo "VPN started successfully."
    else
        echo "Failed to start VPN."
    fi
}

stop_vpn() {
    if [ ! -f "$PID_FILE" ]; then
        echo "VPN is not running."
        exit 1
    fi

    PID=$(cat "$PID_FILE")
    echo "Stopping OpenVPN (PID: $PID)..."

    sudo kill "$PID"
    rm -f "$PID_FILE"

    echo "VPN stopped."
}

status_vpn() {
    if [ -f "$PID_FILE" ]; then
        echo "VPN is running (PID: $(cat $PID_FILE))"
    else
        echo "VPN is not running."
    fi
}

case "$1" in
    start)
        start_vpn
        ;;
    stop)
        stop_vpn
        ;;
    restart)
        stop_vpn
        sleep 1
        start_vpn
        ;;
    status)
        status_vpn
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        echo "Config File at \""$CONFIG_FILE"\""
        exit 1
        ;;
esac