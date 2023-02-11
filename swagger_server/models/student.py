# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.grade_record import GradeRecord  # noqa: F401,E501
from swagger_server import util


class Student(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, first_name: str=None, last_name: str=None, student_id: float=None, grade_record: GradeRecord=None):  # noqa: E501
        """Student - a model defined in Swagger

        :param first_name: The first_name of this Student.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this Student.  # noqa: E501
        :type last_name: str
        :param student_id: The student_id of this Student.  # noqa: E501
        :type student_id: float
        :param grade_record: The grade_record of this Student.  # noqa: E501
        :type grade_record: GradeRecord
        """
        self.swagger_types = {
            'first_name': str,
            'last_name': str,
            'student_id': float,
            'grade_record': GradeRecord
        }

        self.attribute_map = {
            'first_name': 'first_name',
            'last_name': 'last_name',
            'student_id': 'student_id',
            'grade_record': 'GradeRecord'
        }
        self._first_name = first_name
        self._last_name = last_name
        self._student_id = student_id
        self._grade_record = grade_record

    @classmethod
    def from_dict(cls, dikt) -> 'Student':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Student of this Student.  # noqa: E501
        :rtype: Student
        """
        return util.deserialize_model(dikt, cls)

    @property
    def first_name(self) -> str:
        """Gets the first_name of this Student.


        :return: The first_name of this Student.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name: str):
        """Sets the first_name of this Student.


        :param first_name: The first_name of this Student.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self) -> str:
        """Gets the last_name of this Student.


        :return: The last_name of this Student.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        """Sets the last_name of this Student.


        :param last_name: The last_name of this Student.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def student_id(self) -> float:
        """Gets the student_id of this Student.


        :return: The student_id of this Student.
        :rtype: float
        """
        return self._student_id

    @student_id.setter
    def student_id(self, student_id: float):
        """Sets the student_id of this Student.


        :param student_id: The student_id of this Student.
        :type student_id: float
        """
        if student_id is None:
            raise ValueError("Invalid value for `student_id`, must not be `None`")  # noqa: E501

        self._student_id = student_id

    @property
    def grade_record(self) -> GradeRecord:
        """Gets the grade_record of this Student.


        :return: The grade_record of this Student.
        :rtype: GradeRecord
        """
        return self._grade_record

    @grade_record.setter
    def grade_record(self, grade_record: GradeRecord):
        """Sets the grade_record of this Student.


        :param grade_record: The grade_record of this Student.
        :type grade_record: GradeRecord
        """
        if grade_record is None:
            raise ValueError("Invalid value for `grade_record`, must not be `None`")  # noqa: E501

        self._grade_record = grade_record
