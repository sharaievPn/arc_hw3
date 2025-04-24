### Homework 3

## Task #1 - Wrap single application in container
1) Start application - ```bash start_app.sh```
![start app](./assets/start1.png)
2) Send request (any request from homework 2) - 
![send request](./assets/send_request1.png)
3) Check logs
![check logs](./assets/check_logs1.png)
4) Shutdown application and clean environemt - ```podman ps``` -> ```podman stop {hash}``` -> ```podman rm {hash}```
![shutdown environment](./assets/shutdown1.png)

## Task #2 - Multi-container setup with a local network.
1) Start application - ```podman-compose up```
![start app](./assets/start2.png)
2) Send request (any request from homework 2) - 
![send request](./assets/send_request2.png)
3) Check logs
![check logs](./assets/check_logs2.png)
4) Shut down application and clean environment - ```podman-compose down```
![shutdown environment](./assets/shutdown2.png)