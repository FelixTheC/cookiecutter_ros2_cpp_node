#include "rclcpp/rclcpp.hpp"

#pragma once

#ifndef {{cookiecutter.node_file_name|upper}}_HPP
#define {{cookiecutter.node_file_name|upper}}_HPP

class {{cookiecutter.node_class_name}} : public rclcpp::Node
{

public:
    {{cookiecutter.node_class_name}}();

};

#endif