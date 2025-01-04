import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import threading

class KeyboardTalker(Node):
    def __init__(self):
        super().__init__("keyboard_talker")
        self.pub = self.create_publisher(String, "keyboard_input", 10)
        self.create_thread()

    def create_thread(self):
        self.input_thread = threading.Thread(target=self.get_user_input)
        self.input_thread.daemon = True
        self.input_thread.start()

    def get_user_input(self):
        while rclpy.ok():
            try:
                user_input = input()
                if user_input.strip().lower() == "exit":
                    rclpy.shutdown()
                    break
                msg = String()
                msg.data = user_input
                self.pub.publish(msg)
            except EOFError:
                break

def main():
    rclpy.init()
    node = KeyboardTalker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()

