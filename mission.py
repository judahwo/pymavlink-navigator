from pymavlink import mavutil

master = mavutil.mavlink_connection('udp:localhost:14445')

master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" %
      (master.target_system, master.target_component))

flight_mode = 4  

master.mav.command_long_send(
    master.target_system,         
    master.target_component,      
    mavutil.mavlink.MAV_CMD_DO_SET_MODE,  
    0,                            
    mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,  
    flight_mode,           
    0,                            
    0,                            
    0,                            
    0,                            
    0                             
)

master.mav.command_long_send(
    master.target_system, 
    master.target_component, 
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0, 1, 0, 0, 0, 0, 0, 0)

master.mav.send(
    mavutil.mavlink.
    MAVLink_set_position_target_local_ned_message(
        0,
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,
        int(0b100111111000),
        -30, -30, 10,
        0, 0, 0,
        0, 0, 0,
        3.927, 0
    ))

# master.mav.send(
#     mavutil.mavlink.
#     MAVLink_set_position_target_local_ned_message(
#         0,
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_FRAME_LOCAL_NED,
#         int(0b100111111000),
#         -30, 30, 10,
#         0, 0, 0,
#         0, 0, 0,
#         1.5708, 0
#     ))

# master.mav.send(
#     mavutil.mavlink.
#     MAVLink_set_position_target_local_ned_message(
#         0,
#         master.target_system,
#         master.target_component,
#         mavutil.mavlink.MAV_FRAME_LOCAL_NED,
#         int(0b100111111000),
#         0, 0, 0,
#         0, 0, 0,
#         0, 0, 0,
#         5.498, 0
#     ))

# while True:
#     msg = master.recv_match(
#         type='LOCAL_POSITION_NED', blocking=True)
#     print(msg)
