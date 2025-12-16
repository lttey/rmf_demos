import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
import sys
from rclpy.qos import QoSProfile, QoSDurabilityPolicy

class BoolPublisher(Node):
    def __init__(self, value: bool, topic_name: str):
        super().__init__('bool_publisher')

        qos = QoSProfile(
            depth=1,
            durability=QoSDurabilityPolicy.TRANSIENT_LOCAL
        )

        self.publisher_ = self.create_publisher(Bool, topic_name, qos)

        msg = Bool()
        msg.data = value
        self.publisher_.publish(msg)
        self.get_logger().info(
            f"Published to '{topic_name}' (transient local): {msg.data}"
        )

def main(args=None):
    rclpy.init(args=args)

    # Default values
    topic_name = "fire_alarm_trigger"
    value = True

    # Parse topic name (first argument)
    if len(sys.argv) > 1:
        topic_name = sys.argv[1]

    # Parse message value (second argument)
    if len(sys.argv) > 2:
        arg = sys.argv[2].lower()
        if arg in ['true', '1']:
            value = True
        elif arg in ['false', '0']:
            value = False
        else:
            print("Invalid boolean value, using default True")

    node = BoolPublisher(value, topic_name)
    rclpy.spin_once(node, timeout_sec=1)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
