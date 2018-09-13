# Reinforcement Learning for Control Systems
Project Description

Currently, rules (control policy) for the mechanical operations (control loops) of most sophisticated machinery are set by human experts, which require tremendous time and domain expertise. If we can teach machine to learn these rules and reduce the reliance on scarce human experts, that has far-reaching impacts across all manufacturing fields.

The complexity and diversity of control loops in hard technologies like metal 3D printing makes them a good candidate for Reinforcement Learning (RL). RL algorithms usually require a lot of trials and it is expensive and dangerous to run physical trials. But combining RL with simulation will not only optimize the control policy for more efficiency and time saving, it also can disrupt manufacturing by developing new methods that require less complicated machinery.


Use case:

- Scheduling of emergency medicine doctors in inner city hospitals

Deliverable:

Deep reinforcement learning as a service platform that can learn a policy using a specific simulation environment or existing dataset. The service needs to interfaces with the engineer to gather the model and objective function and potentially take advantage of imitation learning and off-policy learning to improve the speed of convergence and gather bounds on each parameter to help reduce search space. The service should take advantage of asynchronous and parallel deep RL techniques to speed up the learning process as well. The accuracy of policy should exceed human generated policy. 

## Motivation for this project format:
- **src** : Put all source code for production within structured directory
- **tests** : Put all source code for testing in an easy to find location
- **configs** : Enable modification of all preset variables within single directory (consisting of one or many config files for separate tasks)
- **data** : Include example a small amount of data in the Github repository so tests can be run to validate installation
- **build** : Include scripts that automate building of a standalone environment
- **static** : Any images or content to include in the README or web framework if part of the pipeline

## Setup
Clone repository and update python path
```
repo_name=Insight_Project_Framework # URL of your new repository
username=mrubash1 # Username for your personal github account
git clone https://github.com/$username/$repo_name
cd $repo_name
echo "export $repo_name=${PWD}" >> ~/.bash_profile
echo "export PYTHONPATH=$repo_name/src:${PYTHONPATH}" >> ~/.bash_profile
source ~/.bash_profile
```
Create new development branch and switch onto it
```
branch_name=dev-readme_requisites-20180905 # Name of development branch, of the form 'dev-feature_name-date_of_creation'}}
git checkout -b $branch_name
git push origin $branch_name
```

## Requisites
- List all packages and software needed to build the environment
- This could include cloud command line tools (i.e. gsutil), package managers (i.e. conda), etc.
```
# Example
- A
- B
- C
```

## Build Environment
- Include instructions of how to launch scripts in the build subfolder
- Build scripts can include shell scripts or python setup.py files
- The purpose of these scripts is to build a standalone environment, for running the code in this repository
- The environment can be for local use, or for use in a cloud environment
- If using for a cloud environment, commands could include CLI tools from a cloud provider (i.e. gsutil from Google Cloud Platform)
```
# Example

# Step 1
# Step 2
```

## Configs
- We recommond using either .yaml or .txt for your config files, not .json
- **DO NOT STORE CREDENTIALS IN THE CONFIG DIRECTORY!!**
- If credentials are needed, use environment variables or HashiCorp's [Vault](https://www.vaultproject.io/)


## Test
- Include instructions for how to run all tests after the software is installed
```
# Example

# Step 1
# Step 2
```

## Run Inference
- Include instructions on how to run inference
- i.e. image classification on a single image for a CNN deep learning project
```
# Example

# Step 1
# Step 2
```

## Build Model
- Include instructions of how to build the model
- This can be done either locally or on the cloud
```
# Example

# Step 1
# Step 2
```

## Serve Model
- Include instructions of how to set up a REST or RPC endpoint 
- This is for running remote inference via a custom model
```
# Example

# Step 1
# Step 2
```

## Analysis
- Include some form of EDA (exploratory data analysis)
- And/or include benchmarking of the model and results
```
# Example

# Step 1
# Step 2
```
