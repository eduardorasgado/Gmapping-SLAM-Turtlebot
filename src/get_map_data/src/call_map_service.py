#! /usr/bin/env python
import rospy
from nav_msgs.srv import GetMap, GetMapRequest

def mapCallback(msg):
    rospy.loginfo("Yeah!")
    print("what")

def main():
    rospy.init_node("map_call_client_service_node")
    
    rospy.wait_for_service("/static_map")
    
    try:
        rospy.loginfo("Execiting client")
        
        mapClient = rospy.ServiceProxy('/static_map', GetMap)
        
        mapRequest = GetMapRequest()
        result = mapClient(mapRequest)
        
        if result:
            rospy.loginfo("EVETHING IS FINE")
            mapResolution = "Resolution: "+str(result.map.info.resolution)
            mapDimensions = "width: "+str(result.map.info.width)+", height: "+str(result.map.info.height)
            mapData = mapResolution+" "+mapDimensions
            rospy.loginfo(mapData)
        
    except Exception as e:
        rospy.logerr("An error haas occurred on client server.")

if __name__=="__main__":
    try:
        main()
    except:
        print("ERROR!")