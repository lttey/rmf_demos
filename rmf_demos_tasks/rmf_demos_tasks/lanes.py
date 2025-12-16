#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy as Durability
import sys

from rmf_fleet_msgs.msg import LaneRequest  # RMF message

class LaneRequestPublisher(Node):
    def __init__(self, fleet_name="tinyRobot", topic="lane_closure_requests"):
        super().__init__('lane_request_publisher')

        # Default QoS
        qos = QoSProfile(
            depth=1,
            durability=Durability.TRANSIENT_LOCAL
        )
        self.publisher = self.create_publisher(LaneRequest, topic, qos)
        self.fleet_name = fleet_name

    def send_request(self, lane_idx: int, is_open: bool):
        msg = LaneRequest()
        msg.fleet_name = self.fleet_name

        if is_open:
            msg.open_lanes = [lane_idx]
            msg.close_lanes = []
        else:
            msg.open_lanes = []
            msg.close_lanes = [lane_idx]

        self.publisher.publish(msg)
        self.get_logger().info(
            f"Published request: {'OPEN' if is_open else 'CLOSE'} lane {lane_idx}"
        )


def main(args=None):
    rclpy.init(args=args)

    # -------- Parse CLI Arguments --------
    if len(sys.argv) != 3:
        print("Usage: lane_request_publisher.py [open|close] <lane_index>")
        return

    action = sys.argv[1].lower()
    lane_idx = int(sys.argv[2])

    if action not in ["open", "close"]:
        print("Error: action must be 'open' or 'close'")
        return

    is_open = (action == "open")
    # -------------------------------------

    node = LaneRequestPublisher()

    node.send_request(lane_idx, is_open)

    rclpy.spin_once(node, timeout_sec=0.2)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
