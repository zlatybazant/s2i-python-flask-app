FROM openshift/base-centos7

# TODO: Put the maintainer name in the image metadata
LABEL maintainer="Jakub Kieryk <jakub@kieryk.me>"

# TODO: Rename the builder environment variable to inform users about application you provide them
ENV FLASK_DEVELOPMENT_SERVER=ON

# TODO: Set labels used in OpenShift to describe the builder image
LABEL io.k8s.description="Platform for serving Python/Flask app " \
      io.k8s.display-name="Zadanie" \
      io.openshift.expose-services="8080:5000" \
      io.openshift.tags="builder,html,flask,python3"

# TODO: Install required packages here:
# RUN yum install -y ... && yum clean all -y
RUN yum -y install epel-release 
RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
RUN yum -y install python3 && yum -y install python3-pip && yum clean all -y
RUN pip3 install flask

# TODO (optional): Copy the builder files into /opt/app-root
# COPY ./<builder_folder>/ /opt/app-root/

# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7 image
# sets io.openshift.s2i.scripts-url label that way, or update that label
LABEL io.openshift.s2i.scripts-url=image:///usr/local/s2i
COPY ./s2i/bin/ /usr/local/s2i
COPY ./app /opt/app-root/app

# TODO: Drop the root user and make the content of /opt/app-root owned by user 1001
RUN chown -R 1001:1001 /opt/app-root

# This default user is created in the openshift/base-centos7 image
USER 1001

# TODO: Set the default port for applications built using this image
#EXPOSE 8080

# TODO: Set the default CMD for the image
CMD ["/usr/local/s2i/usage"]

