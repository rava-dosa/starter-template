## Steps to Run


### For every other change

1. For react frontend, change files in "frontend/src" folder.
2. Then run "npm run prod" in "frontend" folder
3. For python/backend, change file backend/server.py
4. It auto updates itself. 
5. If changes are not reflected
    1. Fresh file is not being served to browser
    2. One reason could be your new js couldn't compile. Soln:- Edit and Recompile
    3. You have closed js hot reload process aka "npm run prod". Soln :- Run the command again
    4. You browser is not loading new js. Soln :- ctrl+shift+r


### First Time

1. Install python and flask.
2. Install npm. What you can do is go [here](https://nodejs.org/dist/v12.16.2/node-v12.16.2-linux-x64.tar.xz), download and extract it. And update path variable in bashrc. Source bashrc. Also set [proxy](https://stackoverflow.com/questions/57202923/npm-install-global-command-proxy-issue)
3. Then go to frontend folder and run
    1. npm install
    2. npm run prod
    3. "npm run prod" will create a file called bundle.js in frontend/dist. Check this.
4. Go to backend folder. Then run python server.py. 
