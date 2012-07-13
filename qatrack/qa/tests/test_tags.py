from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.test.utils import setup_test_environment
from django.utils import unittest,timezone
from qatrack import settings
from qatrack.qa import models,views,forms

from qatrack.qa.templatetags import qa_tags


import utils


#============================================================================
class TestTags(TestCase):
    """
    These tests are only testing the tags return valid strings and not
    actually testing functionality.
    """

    #----------------------------------------------------------------------
    def setUp(self):
        self.unit_test_list = utils.create_unit_test_collection()
    #----------------------------------------------------------------------
    def test_as_qavalue(self):
        form = forms.TestInstanceForm()
        rendered = qa_tags.as_qavalue(form,True)
        self.assertIsInstance(rendered,basestring)

    #----------------------------------------------------------------------
    def test_as_unittestcollections_table(self):
        utcs = models.UnitTestCollection.objects.all()
        rendered = qa_tags.as_unittestcollections_table(utcs)
        self.assertIsInstance(rendered,basestring)
    #----------------------------------------------------------------------
    def test_unreviewed_count(self):
        rendered = qa_tags.as_unreviewed_count(self.unit_test_list)
        self.assertIsInstance(rendered,basestring)
    #----------------------------------------------------------------------
    def test_due_date(self):
        rendered = qa_tags.as_due_date(self.unit_test_list)
        self.assertIsInstance(rendered,basestring)
    #----------------------------------------------------------------------
    def test_as_pass_fail_status(self):
        tli = utils.create_test_list_instance(
            test_list=self.unit_test_list.tests_object,
            unit=self.unit_test_list.unit,
        )
        rendered = qa_tags.as_pass_fail_status(tli)
        self.assertIsInstance(rendered,basestring)
    #----------------------------------------------------------------------
    def test_as_data_attributes(self):
        rendered = qa_tags.as_data_attributes(self.unit_test_list)
        self.assertIsInstance(rendered,basestring)