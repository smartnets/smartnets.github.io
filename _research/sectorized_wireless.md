---
layout: article
title: "Sectorized Directional Wireless Networks"
permalink: /research/sectorized_wireless
key: page-aside
cover: /assets/images/sectorized_networks.png
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

![Sectorized Directional Wireless Networks](/assets/images/sectorized_networks.png)






# Sectorized mmWave Networks

We explore how next-generation wireless systems can exploit **sectorization**—the ability of each infrastructure node to activate multiple directional antennas—to reshape the network and deliver fiber-like speeds. Our work begins by defining a comprehensive **sectorized network model** that captures how each node’s sectors interact to form multi-hop paths, and how interference is influenced by different sector configurations.

Within this model, we compute the **capacity region**, which represents all the traffic demands (or flows) the network can support without overloading. By carefully tuning each node’s sectorization, we can increase total throughput, reduce congestion, and route traffic more efficiently. We formalize this tuning as an **optimization problem**, where given a target network flow, we find the best way to define the sectors. We then delve deeper into how dynamically reconfiguring these sectors can change the *effective* network topology—unlocking even more capacity when traffic patterns vary over time.

A central contribution is our **Even Homogeneous Sectorization** approach, which constructs a bipartite structure in the effective network graph. This structure significantly simplifies capacity calculations, speeds up routing decisions, and makes distributed algorithms easier to implement. 

## Selected Publications

Promponas, P., Chen, T., & Tassiulas, L. *Optimizing Sectorized Wireless Networks: Model, Analysis, and Algorithm*. In 24th International Symposium on Theory, Algorithmic Foundations, and Protocol Design for Mobile Networks and Mobile Computing (MobiHoc '23).

## Demo Video

<video width="720" controls preload="none" poster="/assets/videos/sectorization_demo_thumbnail.png">
  <source src="/assets/videos/sectorization_demo.mp4" type="video/mp4">
  Sorry, your browser can't play this video.
</video>

