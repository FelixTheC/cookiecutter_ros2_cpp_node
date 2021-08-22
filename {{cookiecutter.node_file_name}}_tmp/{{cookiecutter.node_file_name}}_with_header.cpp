#include "{{cookiecutter.node_file_name}}.hpp"


{{cookiecutter.node_class_name}}::{{cookiecutter.node_class_name}}(): Node("{{cookiecutter.node_name}}")
{
    RCLCPP_INFO(get_logger(), "{{cookiecutter.node_class_name}} has been started.");
}


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<{{cookiecutter.node_class_name}}>();

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}