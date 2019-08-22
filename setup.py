from setuptools import setup

setup (
   name = 'compute_graph',
   version = '1.0',
   description = 'Compute graph implementation for Python.',
   author = 'Vitche Research Team Developer',
   author_email = 'developer@vitche.com',
   py_modules = ['compute.graph', 'compute.graph.structure', 'compute.graph.profile', 'compute.graph.activation', 'compute.graph.visualization'],
   install_requires = []
)
