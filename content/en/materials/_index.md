---
title: "Materials"
---

## Chapter I: Kernel Related

### Subtopic 1: I/O Aware & Exact Attention

| Paper                                | Link                                               |
|--------------------------------------|----------------------------------------------------|
| FlashAttention 1, 2, 3               | [PDF](https://arxiv.org/pdf/2205.14135), [PDF](https://arxiv.org/pdf/2307.08691), [PDF](https://arxiv.org/pdf/2407.08608)                                                          |
| PagedAttention (vLLM)                | [PDF](https://arxiv.org/pdf/2309.06180)            |
| SGLang                               | [PDF](https://arxiv.org/pdf/2312.07104)            |
| FlexAttention                        | [PDF](https://arxiv.org/pdf/2412.05496)            |
| FlashInfer                           | [PDF](https://arxiv.org/pdf/2501.01005)            |
| SpargeAttention                      | [PDF](https://arxiv.org/pdf/2502.18137)            |
| SageAttention 1,2                    | [PDF](https://arxiv.org/pdf/2410.02367), [PDF](https://arxiv.org/abs/2411.10958)                                                                                      |

### Subtopic 2: Sparse Attention

| Paper                                | Link                                               |
|--------------------------------------|----------------------------------------------------|
| DejaVu                               | [PDF](https://arxiv.org/pdf/2310.17157)            |
| H2O                                  | [PDF](https://arxiv.org/abs/2306.14048)            |
| SpAttn                               | [PDF](https://arxiv.org/pdf/2012.09852)            |
| MoE                                  | [PDF](https://arxiv.org/pdf/1701.06538)            |
| Deepseek-MoE                         | [PDF](https://arxiv.org/pdf/2201.05596)            |

### Subtopic 3: Kernel Generation & Compiler

| Paper                                | Link                                               |
|--------------------------------------|----------------------------------------------------|
| TVM                                  | [PDF](https://www.usenix.org/system/files/osdi18-chen.pdf)   |
| Ansor                                | [PDF](https://arxiv.org/pdf/2006.06762)            |
| MLIR                                 | [PDF](https://arxiv.org/abs/2002.11054)            |

### Subtopic 4: Execution Optimization/Serving

| Paper                                | Link                                               |
|--------------------------------------|----------------------------------------------------|
| Alpa                                 | [PDF](https://www.usenix.org/system/files/osdi22-zheng-lianmin.pdf)   |
| Orca                                 | [PDF](https://www.usenix.org/system/files/osdi22-yu.pdf)            |
| FlexGen                              | [PDF](https://arxiv.org/pdf/2303.06865)            |
| ZeRO-Offloading                      | [PDF](https://arxiv.org/abs/1910.02054)   |
| Megatron-LM                          | [PDF](https://arxiv.org/abs/1909.08053)            |
| FlashDecoding++                      | [PDF](https://arxiv.org/pdf/2311.01282)            |
| SarathiServe                         | [PDF](https://www.usenix.org/system/files/osdi24-agrawal.pdf)   |

---

## Chapter II: Efficient LLM

### Subtopic 1: LLM 101

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| Attention is All You Need                            | [PDF](https://arxiv.org/abs/1706.03762)            |
| BERT                                                 | [PDF](https://arxiv.org/abs/1810.04805)            |
| GPT-3                                                | [PDF](https://arxiv.org/abs/2005.14165)            |
| Scaling Laws                                         | [PDF](https://arxiv.org/pdf/2001.08361)            |
| RLHF                                                 | [PDF](https://arxiv.org/abs/2203.02155)            |
| PPO/DPO                                              | [PDF](https://arxiv.org/abs/1707.06347) , [PDF](https://arxiv.org/abs/2305.18290)           |


### Subtopic 2: Efficient Inference & Long-context

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| Streaming LLM & DuoAttention                         | [PDF](https://arxiv.org/abs/2309.17453), [PDF](https://arxiv.org/pdf/2410.10819)                                                                                                      |
| MInference                                           | [PDF](https://arxiv.org/abs/2407.02490  )          |
| H2O                                                  | [PDF](https://arxiv.org/abs/2306.14048)            |
| TOVA/KIVI                                            | [PDF](https://arxiv.org/pdf/2401.06104), [PDF](https://arxiv.org/abs/2402.02750)            |
| Speculative Decoding                                 | [PDF](https://arxiv.org/abs/2211.17192), [PDF](https://arxiv.org/abs/2401.10774)             |
| Multi-token prediction: Deepseek-v3                               | [PDF](https://arxiv.org/abs/2412.19437)                                  |

### Subtopic 3: Model Compression (Quant & Pruning)

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| LLM.int8()/GPTQ                                      | [PDF](https://arxiv.org/abs/2208.07339), [PDF](https://arxiv.org/abs/2210.17323)            |
| AWQ                                                  | [PDF](https://arxiv.org/abs/2306.00978)            |
| LLM Pruner                                                | [PDF](https://arxiv.org/abs/2305.11627)            |
| ShearedLlama                                         | [PDF](https://arxiv.org/pdf/2310.06694)            |

### Subtopic 4: Efficient Training

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| ZeRO                                      | [PDF](https://arxiv.org/abs/1910.02054)  |
| Megatron-LM                                                  | [PDF](https://arxiv.org/abs/1909.08053)            |
| LoRA & QLoRA                                                | [PDF](https://arxiv.org/abs/2106.09685), [PDF](https://arxiv.org/abs/2305.14314)            |

### Subtopic 5: Efficient Model Designs

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| Swtich Transformers/Outrageously Large Neural Networks                                      | [PDF](https://arxiv.org/abs/2101.03961), [PDF](https://arxiv.org/abs/1701.06538)  |
| MLA Attention                                                  | [PDF](https://arxiv.org/abs/2412.19437)            |
| Mamba                                                | [PDF](https://arxiv.org/abs/2312.00752)            |


---

## Chapter III: Video Generation

### Subtopic 1: SOTA/Baseline Model

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| CogVideoX                                            | [PDF](https://arxiv.org/pdf/2408.06072)            |
| HunyuanVideo                                                 | [PDF]( https://arxiv.org/pdf/2412.03603 )            |
| WAN                                                | [PDF](https://files.alicdn.com/tpsservice/5c9de1c74de03972b7aa657e5a54756b.pdf)            |
| Seaweed-7B                                         | [PDF]( https://seaweed.video/seaweed.pdf )            |

### Subtopic 2: Optimization Techniques

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| Pruning                                            | [UniCP](https://arxiv.org/pdf/2502.04393)            |
| Cache                                              | [PDF]( https://arxiv.org/pdf/2504.03140 ), need to add more..|
| Compression                                        | [PDF](https://arxiv.org/pdf/2410.10733)            |
| Sparsity                                         | [PDF](  https://arxiv.org/pdf/2502.21079 )            |

### Subtopic 3: Long Video Generation

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| Tuning-Free Multi-Event Long Video Generation                                            | [PDF](https://arxiv.org/pdf/2503.08605)            |
| Long Context Tuning for Video Generation                                              | [PDF]( https://arxiv.org/pdf/2503.10589 )|
| One-Minute Video Generation with Test-Time Training                                        | [PDF](https://www.alphaxiv.org/abs/2504.05298)            |
| SKYREELS-V2: INFINITE-LENGTH FILM GENERATIVE MODEL                                         | [PDF](   https://arxiv.org/pdf/2504.13074 )            |

### Subtopic 4: Video Super Resolution

| Paper                                                | Link                                               |
|------------------------------------------------------|----------------------------------------------------|
| SeedVR                                            | [PDF](https://arxiv.org/abs/2501.01320)            |
| MGLD-VSR                                              | [PDF]( https://arxiv.org/abs/2312.00853 )|
| DynamicScaler                                         | [PDF](   https://arxiv.org/abs/2412.11100 )            |

---

## Chapter IV: Secure LLM

### Subtopic 1: Diffusion Model/Flow Matching

### Subtopic 2: Watermarking

### Subtopic 3: Efficient CNN

### Subtopic 4: Encryption

---

## Chapter V: MLLM Video Understanding

### Subtopic 1: SOTA/Baseline

### Subtopic 2: Optimization Techniques

### Subtopic 3: Algorithm Design
