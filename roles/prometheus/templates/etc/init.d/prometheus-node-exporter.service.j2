#!/bin/bash
#
#
#
# Start on runlevels 3, 4 and 5. Start late, kill early.
# chkconfig: 345 95 05
#
#
RED='\033[0;31m'
NC='\033[0m'
GREEN='\033[0;32m'

program="{{ prometheus_exporters_location }}/{{ prometheus_node_exporter_folder_name }}/node_exporter -collectors.enabled={{ prometheus_node_exporter_enabled_collectors | join(',') }} {% for flag, flag_value in prometheus_node_exporter_config_parameters.iteritems() %}-{{ flag }}={{ flag_value }} {% endfor %}"

# binary program name
prog='node_exporter'

# pid file
pidfile="/var/run/${prog}.pid"

# make sure full path to executable binary is found
! [ -x $progpath ] && echo "$progpath: executable not found" && exit 1

eval_cmd() {
  local rc=$1
  if [ $rc -eq 0 ]; then
    printf "[${GREEN}OK${NC}]\n"
  else
    printf "[${RED}FAILED${NC}]\n"
  fi
  return $rc
}

start() {
  pids=`pidof $prog`
  if [ -n "$pids" ]; then
    echo "$prog (pid $pids) is already running"
    return 0
  fi
  printf "%-50s%s" "Starting $prog: " ''
  daemonize $program
  eval_cmd $?
}

stop() {
  pids=`pidof $prog`
  if !([ -n "$pids" ]); then
    echo "$prog not running"
    return 0
  fi
  printf "%-50s%s" "Stopping $prog: " ''
  rm -f $pidfile
  kill -9 $pids
  eval_cmd $?
}

status() {
  pids=`pidof $prog`
  if [ -n "$pids" ]; then
    echo "$prog (pid $pids) is running"
  else
    echo "$prog is stopped"
  fi
}

case $1 in
  start)
    start
    ;;
  stop)
    stop
    ;;
  status)
    status
    ;;
  restart)
    stop
    sleep 1
    start
    ;;
  *)
    echo "Usage: $0 {start|stop|status|restart}"
    exit 1
esac

exit $?

