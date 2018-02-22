from behave import *


@given(u'I am on the asos.com website')
def step_impl(context):

    # Go to the asos.com
    context.basePageObject.get()