from behave import *


@when(u'I select country from the dropdown')
def step_impl(context):
    context.commonPage.selectCountryFromDropdown()


@then(u'I am on the UK site')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I am on the UK site')