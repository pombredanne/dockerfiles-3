FROM ocaml/opam:debian-stable_ocaml-4.02.3  
RUN sudo -u opam sh -c "opam depext -u tlstunnel" && \  
sudo -u opam sh -c "opam install -y -j 2 -v tlstunnel"

