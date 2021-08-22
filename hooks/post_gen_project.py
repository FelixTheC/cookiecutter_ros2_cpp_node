#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@created: 14.08.21
@author: felix
"""
import os
from collections import OrderedDict
from pathlib import Path
import shutil

context: OrderedDict = {{cookiecutter}}


def ask_more_questions(question=None):
    return input(question)

create_headerfile = ask_more_questions('Do you want to split into .cpp and .hpp [false]: ')
context['create_headerfile'] = create_headerfile or False

if context["create_headerfile"]:
    deployment_prod_or_dev_file = ask_more_questions(
        f'Where you want to put your headerfile: [{context["final_destination"]}]: ')
    context['header_file_path'] = (deployment_prod_or_dev_file or context["final_destination"])


if context["create_headerfile"] and "header_file_path" in context:
    source_dir_header = Path.cwd() / Path("{{cookiecutter.node_file_name}}.hpp")
    target_dir_header = context['header_file_path']

    shutil.move(source_dir_header.as_posix(), target_dir_header)

    source_dir = Path.cwd() / Path("{{cookiecutter.node_file_name}}_with_header.cpp")
    target_dir = "{{ cookiecutter.final_destination }}"

    shutil.move(source_dir.as_posix(), target_dir)

    os.rename((target_dir / Path("{{cookiecutter.node_file_name}}_with_header.cpp")).as_posix(),
              (target_dir / Path("{{cookiecutter.node_file_name}}.cpp")).as_posix())

else:
    source_dir = Path.cwd() / Path("{{cookiecutter.node_file_name}}.cpp")
    target_dir = "{{ cookiecutter.final_destination }}"

    shutil.move(source_dir.as_posix(), target_dir)

os.chdir(Path.cwd().parent)
for folder in Path.cwd().glob('*'):
    if folder.name == '{{cookiecutter.node_file_name}}_tmp':
        shutil.rmtree(folder)
