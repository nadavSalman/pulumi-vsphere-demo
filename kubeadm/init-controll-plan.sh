#
sudo kubeadm init --pod-network-cidr=10.244.0.0/16 --upload-certs --kubernetes-version=v1.26.0 --control-plane-endpoint=192.168.103.198 --cri-socket unix:///run/containerd/containerd.sock --v=5
#

Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

You can now join any number of the control-plane node running the following command on each as root:

  kubeadm join 192.168.103.198:6443 --token 1uzx39.3vzchijxw2gs6yak \
	--discovery-token-ca-cert-hash sha256:032707d79c0a8c1b2731525d45085702b499f893f02f3fa70b354ec3b300c0f7 \
	--control-plane --certificate-key 097217eb96349239e10ea2f4b205db51c29bbc914c40434060c6e43b89a08dc8

Please note that the certificate-key gives access to cluster sensitive data, keep it secret!
As a safeguard, uploaded-certs will be deleted in two hours; If necessary, you can use
"kubeadm init phase upload-certs --upload-certs" to reload certs afterward.

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 192.168.103.198:6443 --token 1uzx39.3vzchijxw2gs6yak \
	--discovery-token-ca-cert-hash sha256:032707d79c0a8c1b2731525d45085702b499f893f02f3fa70b354ec3b300c0f7 




#
kubectl proxy --port=8080
#



