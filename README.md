# KubernetesProject
This is Simple Webapp to take Feedback

Frontend: Html,css,Js
Backend: Flask
Docker, Kubernetes via Minikube


The Kubectl in use

![Photo](photo/elvate%201.png)

The UI result of the pod running
![Photo](photo/elvate%202.png)



To run 
Build dockerfile :
              `docker build -t feedback-app:latest . `
Run Dockerfile :
             `docker run -p 5000:5000 feedback-app    `
Push to registry:
            `docker push YOurUSernamefeedback-app:latest`
            OR
Pull from registry
            `docker pull shrivatsa54/feedback-app:latest`

To run K8's
1. Minikube Start
2.In terminal :
          `kubectl apply -f deployment.yaml`
          `kubectl apply -f service.yaml`
3.To expose URL: 
           `minikube service feedback-app-service`