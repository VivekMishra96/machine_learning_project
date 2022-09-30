# machine_learning_project

### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)


'''
Creating conda environment
```
conda create -p venv python==3.7 -y
```
```
conda activate venv/
```
OR 
```
conda activate venv
```

```
pip install -r requirements.txt
```

To Add files to git
```
git add .
```

OR
```
git add <file_name>
```

> Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status 
```
git status
```

'''
To check all version maintained by git
'''

'''
git log
'''

'''
git commit -m "message"
```

To send version /changes to github
'''
git puch origin main
'''

To check remote url
 '''
 git remote -v 
 '''

 To setup CI/CD pipeline in heroku we need to 3 information

 1.HEROKU_EMAIL=starvivek1996@gmail.com
 2.HEROKU_API_KEY=300d556a-5bf2-4eda-9a1e-7a358fa0da5e
 3.HEROKU_APP_NAME=first2ml


BUILD DOCKER IMAGE 
'''
docker build -t <image_name>:<tagname> .
'''
> Note:Image name for dockere must be lower case

To check the docker images
'''
docker images
'''

To the docker images
'''
docker run -p 5000:5000 -e PORT=5000 faf6adf45d9b
'''

To check running container in docker
'''
docker ps
'''

To stop docker container
'''
docker stop <container_id>

Install ipykernel

'''
pip install ipykernel
'''