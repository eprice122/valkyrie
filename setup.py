from setuptools import find_packages, setup  # type: ignore

reqs = list()
with open("requirements.txt", "r") as f:
    for line in f.readlines():
        reqs.append(line.strip())

setup(
    name="valkyrie",
    description="Backend system management",
    packages=find_packages(),
    # package_data={"sierra": ["py.typed"]},
    install_requires=reqs,
    zip_safe=False,
)
