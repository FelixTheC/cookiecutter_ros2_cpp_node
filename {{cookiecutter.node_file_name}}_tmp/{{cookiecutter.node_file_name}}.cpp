#include "rclcpp/rclcpp.hpp"


class {{cookiecutter.node_class_name}} : public rclcpp::Node
{
public:
    {{cookiecutter.node_class_name}}(): Node("{{cookiecutter.node_name}}")
    {
        RCLCPP_INFO(get_logger(), "Hello Cpp Node");
    }

};


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<{{cookiecutter.node_class_name}}>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}