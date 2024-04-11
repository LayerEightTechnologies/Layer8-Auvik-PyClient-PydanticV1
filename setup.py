# coding: utf-8

"""
Auvik API

To use the Auvik APIs, you’ll need a <a href=\"https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\" target=\"_blank\">valid Auvik user and the user’s API key</a>. The user must also have the correct <a href=\" https://support.auvik.com/hc/en-us/articles/115002815966\" target=\"_blank\">role permissions</a>.<br>     <br>     Note: The word <i>tenant</i> as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.<br><br>All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061<br><br>To find out more about Auvik’s APIs, <a href=\"https://support.auvik.com/hc/en-us/articles/360017965092\" target=\"_blank\">click here.</a>

The version of the OpenAPI document: v1
Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "layer8-auvik-api-client"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, <= 2.2.1",
    "python-dateutil",
    "pydantic >= 1.10.5, < 2",
    "aenum",
]

setup(
    name=NAME,
    version=VERSION,
    description="Auvik API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Auvik API"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type="text/markdown",
    long_description="""\
    To use the Auvik APIs, you’ll need a &lt;a href&#x3D;\&quot;https://support.auvik.com/hc/en-us/articles/204309114-#topic_generate\&quot; target&#x3D;\&quot;_blank\&quot;&gt;valid Auvik user and the user’s API key&lt;/a&gt;. The user must also have the correct &lt;a href&#x3D;\&quot; https://support.auvik.com/hc/en-us/articles/115002815966\&quot; target&#x3D;\&quot;_blank\&quot;&gt;role permissions&lt;/a&gt;.&lt;br&gt;     &lt;br&gt;     Note: The word &lt;i&gt;tenant&lt;/i&gt; as it appears in the API descriptions means one of Auvik’s supported tenant types: multi-client or client.&lt;br&gt;&lt;br&gt;All date formats are formatted in the format of YYYY-MM-DDTHH:MM:SS.sssZ, as describe in ISO 8061&lt;br&gt;&lt;br&gt;To find out more about Auvik’s APIs, &lt;a href&#x3D;\&quot;https://support.auvik.com/hc/en-us/articles/360017965092\&quot; target&#x3D;\&quot;_blank\&quot;&gt;click here.&lt;/a&gt;
    """,  # noqa: E501
    package_data={"layer8_auvik_api_client": ["py.typed"]},
)
