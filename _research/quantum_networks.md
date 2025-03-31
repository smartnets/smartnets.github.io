---
layout: article
title: "Quantum Networks"
permalink: /research/quantum_networks
key: page-aside
cover: /assets/images/quantum_networks.jpg
aside:
  # Set it to true for sidebar
  toc: false
article:
  type: normal
  show_cover: false
  show_excerpt: true
  show_readmore: true
  show_info: true
show_date: false
---

![/assets/images/quantum_networks.jpg](/assets/images/quantum_networks.jpg)










# Optimizing and Modeling Quantum Entanglement Networks

Quantum networks are systems of interconnected quantum devices that share entangled qubits across distances. These entanglement-based links form the foundation of quantum communication, enabling powerful capabilities such as quantum key distribution (QKD), distributed quantum computing, and high-precision quantum sensing. However, entanglement is fragile—loss and decoherence quickly degrade it over long distances, making entanglement distribution a critical research challenge.
           
            
A key component of such networks is the quantum repeater. These devices extend the range of entanglement by dividing long links into shorter segments and performing entanglement swapping and purification at intermediate nodes. Another core element is the <strong>quantum switch</strong>, which dynamically manages entanglement resources and efficiently connects users based on demand.
            
            
These network elements are essential because large-scale, monolithic quantum processors are currently infeasible. Quantum systems are hard to scale due to hardware limitations and error rates. Instead, by connecting smaller quantum devices through entangled links, we can build scalable, modular architectures. My research models these entanglement distribution networks and develops scheduling and optimization methods for improving their capacity, performance, and robustness.
        

            
## Selected Publications
      
            
Valls, V., Promponas, P., & Tassiulas, L. A Brief Introduction to Quantum Network Control. IEEE Communications Magazine.
            
Promponas, P., Valls, V., & Tassiulas, L. Maximizing Entanglement Rates via Efficient Memory Management in Flexible Quantum Switches. IEEE Journal on Selected Areas in Communications, Special Issue on “The Quantum Internet: principles, protocols, and architectures”.
        
Valls, V., Promponas, P., & Tassiulas, L. On the Capacity of the Quantum Switch with and without Entanglement Decoherence. IEEE Communications Letters.
        

# Distributed Quantum Computing and Compiler Design
        


As quantum computing technology evolves, a single quantum processor may not be able to handle the size and complexity of large-scale quantum applications. To address this, <strong>Distributed Quantum Computing (DQC)</strong> has emerged as a promising architecture that connects multiple quantum processors via quantum links to operate as a unified computational platform.
            
One of the core challenges in DQC is enabling seamless execution of quantum circuits across physically separated QPUs. This requires careful handling of two critical compilation tasks:
                
*Initial Qubit Mapping*: Strategically assigning logical qubits in the circuit to the physical qubits available across the networked QPUs, in a way that anticipates and minimizes costly inter-QPU operations.
*Qubit Routing*: Managing the generation and use of entanglement links, scheduling quantum teleportation operations, and injecting SWAP gates to move qubits efficiently across and within QPUs.
                
Our work is focused on developing compilation frameworks that jointly consider these aspects under realistic system constraints, such as limited link fidelity, qubit decoherence, and network congestion. The goal is to enable efficient, scalable, and reliable execution of quantum circuits in distributed settings.
            
The GIF below demonstrates a scenario with two QPUs connected by a single quantum link. It visualizes some of the actions that the compiler can perform: locally SWAPping logical qubits within a QPU, and performing qubit and gate teleportations across QPUs. These actions are taken to execute a quantum circuit, which is represented internally as a Directed Acyclic Graph (DAG).
           


![Distributed Quantum Compiler Demo](/assets/videos/quantum-demo.gif)


## Selected Publications

Promponas, P., Mudvari, A., Della Chiesa, L., Polakos, P., Samuel, L., & Tassiulas, L. Compiler for Distributed Quantum Computing: a Reinforcement Learning Approach. 2025 IEEE International Conference on Communications (ICC ‘25).
        

        
