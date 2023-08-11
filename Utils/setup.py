from pathlib import Path
from setuptools import find_packages, setup
root_dir = Path(__file__).parent
install_requires = (root_dir / "requirements.txt").read_text().splitlines()

setup(name="fmutils",
      version="0.0.1",
      python_requires=">=3.8.0",
      description="A toolkit for Fortemedia Samsoft",
      packages=find_packages(),
      include_package_data=True,
      author="richardtsai",
      author_email="richard.tsai@fortemedia.com",
      install_requires=install_requires,
      entry_points={
          "console_scripts": [
              "rms=eval.rms:main",
              "erle=eval.erle_plotter:main",
              "polar_pattern=eval.polar_pattern:main",
              "spanalyze=eval.spanalyze:main",
              "spview=eval.spview:main",
              "qconvertor=tuning.qconvertor:main",
              "drc_curve=tuning.drc_curve:main",
              "duration=cli.duration:main",
              "generate_sine=cli.generate_sine:main",
              "vecconvertor=vec.convertor:main",
              "vecformat=vec.format:main",
              "veceditor=vec.editor:main",
              "vecvalidator=vec.validator:main"
              ]
          }
      )
