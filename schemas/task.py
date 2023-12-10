"""
File: task.py
Author: Anderson Monteiro
Date: 10/12/2023
Description: Here we create Pydantic classes to control data types and type
hints in the application. The following schemas are task schemas, child
attributes of a project.
"""
import datetime

from pydantic import BaseModel
from typing import List

from model.task import Task


class TaskSchema(BaseModel):
    """
  Defines how a task must be represented
 """

    # identity attributes
    name: str = "Avulso Inicial"
    description: str = ("Projeto de Lei do Senador Acácio que altera a Lei do "
                        "Genocídio")

    # page layout attributes
    header: float = 0.5
    footer: float = 0.5
    line_overlap: float = 0.5
    line_margin: float = 0.5
    char_margin: float = 0.5
    page_numbers: str = "1-25"
    resulting_text: str = "Here goes a really long text."
    tokenized_text: str = "Here goes a lot of words in list."

    # relationship


class TaskSearchSchema(BaseModel):
    name: str = "Substitutivo do Relator"


class ListTaskSchema(BaseModel):
    tasks: List[TaskSchema]


class TaskViewSchema(BaseModel):
    """
        Defines how a task will be represented
    """
    id: int = 1
    name: str = "Emendas propostas pelo governo"
    description: str = "Emendas Fazenda, MGI e SRI."


class TaskDeletionSchema(BaseModel):
    """
    Defines the data structure from the return message from a DELETE request.
    """
    message: str
    name: str


def show_task(task: Task):
    """
        Returns a representation of a task
    """
    return {
        "id": task.id,
        "name": task.name,
        "header": task.header,
        "footer": task.footer,
        "line_overlap": task.line_overlap,
        "line_margin": task.line_margin,
        "char_margin": task.char_margin,
        "page_numbers": task.page_numbers,
        "resulting_text": task.resulting_text,
        "tokenized_text": task.tokenized_text
    }


def list_tasks(tasks: List[Task]):
    result = []
    for task in tasks:
        result.append({
            "name": task.name,
        })
    return {"tasks": result}
