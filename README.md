# cookiecutter_ros2_cpp_node
Cookiecutter project which creates a Node template file


## How to use
- install cookiecutter `pip install cookiecutter`
- then
- `cookiecutter https://github.com/FelixTheC/cookiecutter_ros2_python_node.git`
- you will then see `node_file_name [new_node]:` in the terminal
  - the value inside of the `[..]` is the default value

| Parameter         | Description                       |
| :-------------     |   :-------------:                 |
|node_file_name     |   the filename of the new node    |
|node_class_name    |   the class name of the Node (the default value should fit)|
|node_name          |   the value inside of `super().__init__(<node_name>)`|
|ros2_node          |   don't change the default value  |
|final_destination  |   the path to where put your new node file (see default for more informations)|


### Example file with only default values
- filename `new_node.cpp`
```cpp
#include "rclcpp/rclcpp.hpp"


class NewNode : public rclcpp::Node
{
public:
    NewNode(): Node("new_node")
    {
        RCLCPP_INFO(get_logger(), "Hello Cpp Node");
    }

};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<NewNode>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
```
