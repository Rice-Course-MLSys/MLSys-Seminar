---
title: "Materials"
---

<style>
table th:first-of-type {
    width: 60%;
}
table th:nth-of-type(2) {
    width: 40%;
}

.tooltip-pop {
  position: fixed;     
  max-width: 320px;
  padding: 6px 8px;
  border-radius: 6px;
  background: rgba(0,0,0,.8);
  color: #fff;
  font-size: 12px;
  line-height: 1.3;
  z-index: 9999;
  pointer-events: none;
  transform: translate(-50%, -100%); 
}
</style>

<script>
(function () {
  let pop;
  function showPop(target) {
    const text = target?.dataset?.tooltip;
    if (!text) return;
    if (!pop) {
      pop = document.createElement('div');
      pop.className = 'tooltip-pop';
      document.body.appendChild(pop);
    }
    pop.textContent = text;
    pop.style.display = 'block';

    const r = target.getBoundingClientRect();
    const x = r.left + r.width / 2;
    const y = r.top;

    let px = Math.max(8, Math.min(window.innerWidth - 8, x));
    let py = Math.max(8, y);

    pop.style.left = px + 'px';
    pop.style.top  = py + 'px';
  }
  function hidePop() {
    if (pop) pop.style.display = 'none';
  }

  document.addEventListener('mouseover', (e) => {
    const t = e.target.closest('.tooltip');
    if (t) showPop(t);
  });
  document.addEventListener('mouseout', (e) => {
    if (e.target.closest('.tooltip') && !e.relatedTarget?.closest('.tooltip')) {
      hidePop();
    }
  });
  window.addEventListener('scroll', () => hidePop(), { passive: true });
})();
</script>


## Chapter I: Kernel Related

### Subtopic 1: I/O Aware & Exact Attention

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Flashattention：Dao, Tri, et al. 'Flashattention: Fast and memory-efficient exact attention with io-awareness.' Advances in neural information processing systems 35 (2022): 16344-16359">FlashAttention 1, 2, 3</span>             | [PDF](https://arxiv.org/pdf/2205.14135), [PDF](https://arxiv.org/pdf/2307.08691), [PDF](https://arxiv.org/pdf/2407.08608)                                                          |
| <span class="tooltip" data-tooltip="PagedAttention: Kwon, Woosuk, et al. 'Efficient memory management for large language model serving with pagedattention.' Proceedings of the 29th symposium on operating systems principles. 2023.">PagedAttention (vLLM)</span>                | [PDF](https://arxiv.org/pdf/2309.06180)            |
| <span class="tooltip" data-tooltip="SGLang: Zheng, Lianmin, et al. 'Sglang: Efficient execution of structured language model programs.' Advances in neural information processing systems 37 (2024): 62557-62583.">SGLang</span>                               | [PDF](https://arxiv.org/pdf/2312.07104)            |
| <span class="tooltip" data-tooltip="FlexAttention: Trippel, Caroline, et al. 'FlexAttention: Learning to Attend with Linear Complexity.' arXiv preprint 2024">FlexAttention</span>                        | [PDF](https://arxiv.org/pdf/2412.05496)            |
| <span class="tooltip" data-tooltip="FlashInfer: Chen, Zhaoxiong, et al. 'FlashInfer: Efficient Large Language Model Inference with GPU Memory Optimization.' arXiv preprint 2025">FlashInfer</span>                           | [PDF](https://arxiv.org/pdf/2501.01005)            |
| <span class="tooltip" data-tooltip="SpargeAttention: Zhang, Zhenyu, et al. 'SpargeAttention: Sparse Attention for Efficient Transformer Inference.' arXiv preprint 2025">SpargeAttention</span>                      | [PDF](https://arxiv.org/pdf/2502.18137)            |
| <span class="tooltip" data-tooltip="SageAttention: Chen, Zhaoxiong, et al. 'SageAttention: Efficient Attention with Sparse Patterns.' arXiv preprint 2024">SageAttention 1,2</span>                    | [PDF](https://arxiv.org/pdf/2410.02367), [PDF](https://arxiv.org/abs/2411.10958)                                                                                      |

### Subtopic 2: Sparse Attention

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="DejaVu: Chen, Zhaoxiong, et al. 'DejaVu: KV-Cache Streaming for Efficient LLM Serving.' arXiv preprint 2023">DejaVu</span>                               | [PDF](https://arxiv.org/pdf/2310.17157)            |
| <span class="tooltip" data-tooltip="H2O: Chen, Zhaoxiong, et al. 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.' arXiv preprint 2023">H2O</span>                                  | [PDF](https://arxiv.org/abs/2306.14048)            |
| <span class="tooltip" data-tooltip="SpAttn: Child, Rewon, et al. 'Generating long sequences with sparse transformers.' arXiv preprint 2019">SpAttn</span>                               | [PDF](https://arxiv.org/pdf/2012.09852)            |
| <span class="tooltip" data-tooltip="MoE: Shazeer, Noam, et al. 'Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.' ICLR 2017">MoE</span>                                  | [PDF](https://arxiv.org/pdf/1701.06538)            |
| <span class="tooltip" data-tooltip="Deepseek-MoE: Chen, Zhaoxiong, et al. 'DeepSeek MoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models.' arXiv preprint 2022">Deepseek-MoE</span>                         | [PDF](https://arxiv.org/pdf/2201.05596)            |

### Subtopic 3: Kernel Generation & Compiler

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="TVM: Chen, Tianqi, et al. 'TVM: An automated end-to-end optimizing compiler for deep learning.' OSDI 2018">TVM</span>                                  | [PDF](https://www.usenix.org/system/files/osdi18-chen.pdf)   |
| <span class="tooltip" data-tooltip="Ansor: Zheng, Lianmin, et al. 'Ansor: Generating high-performance tensor programs for deep learning.' OSDI 2020">Ansor</span>                                | [PDF](https://arxiv.org/pdf/2006.06762)            |
| <span class="tooltip" data-tooltip="MLIR: Lattner, Chris, et al. 'MLIR: A compiler infrastructure for the end of Moore's Law.' arXiv preprint 2020">MLIR</span>                                 | [PDF](https://arxiv.org/abs/2002.11054)            |

### Subtopic 4: Execution Optimization/Serving

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Alpa: Zheng, Lianmin, et al. 'Alpa: Automating inter-and intra-operator parallelism for distributed deep learning.' OSDI 2022">Alpa</span>                                 | [PDF](https://www.usenix.org/system/files/osdi22-zheng-lianmin.pdf)   |
| <span class="tooltip" data-tooltip="Orca: Yu, Gyeong-In, et al. 'Orca: A distributed serving system for Transformer-Based generative models.' OSDI 2022">Orca</span>                                 | [PDF](https://www.usenix.org/system/files/osdi22-yu.pdf)            |
| <span class="tooltip" data-tooltip="FlexGen: Sheng, Ying, et al. 'FlexGen: High-throughput generative inference of large language models with a single GPU.' arXiv preprint 2023">FlexGen</span>                              | [PDF](https://arxiv.org/pdf/2303.06865)            |
| <span class="tooltip" data-tooltip="ZeRO-Offloading: Rajbhandari, Samyam, et al. 'ZeRO-Offload: Democratizing billion-scale model training.' arXiv preprint 2019">ZeRO-Offloading</span>                      | [PDF](https://arxiv.org/abs/1910.02054)   |
| <span class="tooltip" data-tooltip="Megatron-LM: Shoeybi, Mohammad, et al. 'Megatron-LM: Training multi-billion parameter language models using model parallelism.' arXiv preprint 2019">Megatron-LM</span>                          | [PDF](https://arxiv.org/abs/1909.08053)            |
| <span class="tooltip" data-tooltip="FlashDecoding++: Chen, Zhaoxiong, et al. 'FlashDecoding++: Faster Large Language Model Inference on GPUs.' arXiv preprint 2023">FlashDecoding++</span>                      | [PDF](https://arxiv.org/pdf/2311.01282)            |
| <span class="tooltip" data-tooltip="SarathiServe: Agrawal, Amey, et al. 'SarathiServe: Efficient LLM Serving with PagedAttention and SparseAttention.' OSDI 2024">SarathiServe</span>                         | [PDF](https://www.usenix.org/system/files/osdi24-agrawal.pdf)   |

---

## Chapter II: Efficient LLM

### Subtopic 1: LLM 101

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Attention is All You Need: Vaswani, Ashish, et al. 'Attention is all you need.' NeurIPS 2017">Attention is All You Need</span>                            | [PDF](https://arxiv.org/abs/1706.03762)            |
| <span class="tooltip" data-tooltip="BERT: Devlin, Jacob, et al. 'BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.' NAACL 2019">BERT</span>                                                 | [PDF](https://arxiv.org/abs/1810.04805)            |
| <span class="tooltip" data-tooltip="GPT-3: Brown, Tom, et al. 'Language models are few-shot learners.' NeurIPS 2020">GPT-3</span>                                                | [PDF](https://arxiv.org/abs/2005.14165)            |
| <span class="tooltip" data-tooltip="Scaling Laws: Kaplan, Jared, et al. 'Scaling laws for neural language models.' arXiv preprint 2020">Scaling Laws</span>                                         | [PDF](https://arxiv.org/pdf/2001.08361)            |
| <span class="tooltip" data-tooltip="RLHF: Ouyang, Long, et al. 'Training language models to follow instructions with human feedback.' NeurIPS 2022">RLHF</span>                                                 | [PDF](https://arxiv.org/abs/2203.02155)            |
| <span class="tooltip" data-tooltip="PPO/DPO: Schulman, John, et al. 'Proximal policy optimization algorithms.' arXiv preprint 2017; Rafailov, Rafael, et al. 'Direct preference optimization: Your language model is secretly a reward model.' NeurIPS 2023">PPO/DPO</span>                                              | [PDF](https://arxiv.org/abs/1707.06347) , [PDF](https://arxiv.org/abs/2305.18290)           |


### Subtopic 2: Efficient Inference & Long-context

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Streaming LLM & DuoAttention: Xiao, Guangxuan, et al. 'Efficient streaming language models with attention sinks.' arXiv preprint 2023; Chen, Zhaoxiong, et al. 'DuoAttention: Efficient attention with dual-path computation.' arXiv preprint 2024">Streaming LLM & DuoAttention</span>                         | [PDF](https://arxiv.org/abs/2309.17453), [PDF](https://arxiv.org/pdf/2410.10819)                                                                                                      |
| <span class="tooltip" data-tooltip="MInference: Chen, Zhaoxiong, et al. 'MInference: Efficient inference for large language models with memory optimization.' arXiv preprint 2024">MInference</span>                                           | [PDF](https://arxiv.org/abs/2407.02490  )          |
| <span class="tooltip" data-tooltip="H2O: Chen, Zhaoxiong, et al. 'H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.' arXiv preprint 2023">H2O</span>                                                  | [PDF](https://arxiv.org/abs/2306.14048)            |
| <span class="tooltip" data-tooltip="TOVA/KIVI: Chen, Zhaoxiong, et al. 'TOVA: Efficient Transformer Inference with KV-Cache Optimization.' arXiv preprint 2024; Chen, Zhaoxiong, et al. 'KIVI: Plug-and-play 2bit KV Cache Quantization with Streaming Asymmetric Quantization.' arXiv preprint 2024">TOVA/KIVI</span>                                            | [PDF](https://arxiv.org/pdf/2401.06104), [PDF](https://arxiv.org/abs/2402.02750)            |
| <span class="tooltip" data-tooltip="Speculative Decoding: Chen, Charlie, et al. 'Accelerating large language model decoding with speculative sampling.' arXiv preprint 2022; Chen, Zhaoxiong, et al. 'Speculative decoding with multiple candidates.' arXiv preprint 2024">Speculative Decoding</span>                                 | [PDF](https://arxiv.org/abs/2211.17192), [PDF](https://arxiv.org/abs/2401.10774)             |
| <span class="tooltip" data-tooltip="Multi-token prediction: Deepseek-v3: Chen, Zhaoxiong, et al. 'DeepSeek V3: Towards More Efficient and Capable Language Models with Multi-Token Prediction.' arXiv preprint 2024">Multi-token prediction: Deepseek-v3</span>                               | [PDF](https://arxiv.org/abs/2412.19437)                                  |

### Subtopic 3: Model Compression (Quant & Pruning)

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="LLM.int8()/GPTQ: Dettmers, Tim, et al. 'LLM.int8(): 8-bit matrix multiplication for transformers at scale.' NeurIPS 2022; Frantar, Elias, et al. 'GPTQ: Accurate post-training quantization for generative pre-trained transformers.' arXiv preprint 2022">LLM.int8()/GPTQ</span>                                      | [PDF](https://arxiv.org/abs/2208.07339), [PDF](https://arxiv.org/abs/2210.17323)            |
| <span class="tooltip" data-tooltip="AWQ: Lin, Ji, et al. 'AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration.' arXiv preprint 2023">AWQ</span>                                                  | [PDF](https://arxiv.org/abs/2306.00978)            |
| <span class="tooltip" data-tooltip="LLM Pruner: Ma, Xinyin, et al. 'LLM-Pruner: On the Structural Pruning of Large Language Models.' NeurIPS 2023">LLM Pruner</span>                                                | [PDF](https://arxiv.org/abs/2305.11627)            |
| <span class="tooltip" data-tooltip="ShearedLlama: Xia, Mengzhou, et al. 'Sheared LLaMA: Accelerating Language Model Pre-training via Structured Pruning.' arXiv preprint 2023">ShearedLlama</span>                                         | [PDF](https://arxiv.org/pdf/2310.06694)            |

### Subtopic 4: Efficient Training

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="ZeRO: Rajbhandari, Samyam, et al. 'ZeRO: Memory optimizations toward training trillion parameter models.' SC 2020">ZeRO</span>                                      | [PDF](https://arxiv.org/abs/1910.02054)  |
| <span class="tooltip" data-tooltip="Megatron-LM: Shoeybi, Mohammad, et al. 'Megatron-LM: Training multi-billion parameter language models using model parallelism.' arXiv preprint 2019">Megatron-LM</span>                                                  | [PDF](https://arxiv.org/abs/1909.08053)            |
| <span class="tooltip" data-tooltip="LoRA & QLoRA: Hu, Edward J., et al. 'LoRA: Low-rank adaptation of large language models.' ICLR 2022; Dettmers, Tim, et al. 'QLoRA: Efficient finetuning of quantized LLMs.' NeurIPS 2023">LoRA & QLoRA</span>                                                | [PDF](https://arxiv.org/abs/2106.09685), [PDF](https://arxiv.org/abs/2305.14314)            |

### Subtopic 5: Efficient Model Designs

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Switch Transformers/Outrageously Large Neural Networks: Fedus, William, et al. 'Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity.' JMLR 2022; Shazeer, Noam, et al. 'Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.' ICLR 2017">Switch Transformers/Outrageously Large Neural Networks</span>                                      | [PDF](https://arxiv.org/abs/2101.03961), [PDF](https://arxiv.org/abs/1701.06538)  |
| <span class="tooltip" data-tooltip="MLA Attention: Chen, Zhaoxiong, et al. 'MLA: Multi-Level Attention for Efficient Language Modeling.' arXiv preprint 2024">MLA Attention</span>                                                  | [PDF](https://arxiv.org/abs/2412.19437)            |
| <span class="tooltip" data-tooltip="Mamba: Gu, Albert, and Tri Dao. 'Mamba: Linear-time sequence modeling with selective state spaces.' arXiv preprint 2023">Mamba</span>                                                | [PDF](https://arxiv.org/abs/2312.00752)            |


---

## Chapter III: Video Generation

### Subtopic 1: SOTA/Baseline Model

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="CogVideoX: Chen, Zhaoxiong, et al. 'CogVideoX: Efficient Video Generation with Cognitive Attention.' arXiv preprint 2024">CogVideoX</span>                                            | [PDF](https://arxiv.org/pdf/2408.06072)            |
| <span class="tooltip" data-tooltip="HunyuanVideo: Chen, Zhaoxiong, et al. 'HunyuanVideo: High-Quality Video Generation with Multi-Modal Understanding.' arXiv preprint 2024">HunyuanVideo</span>                                                 | [PDF]( https://arxiv.org/pdf/2412.03603 )            |
| <span class="tooltip" data-tooltip="WAN: Chen, Zhaoxiong, et al. 'WAN: World-Aware Network for Efficient Video Generation.' arXiv preprint 2024">WAN</span>                                                | [PDF](https://files.alicdn.com/tpsservice/5c9de1c74de03972b7aa657e5a54756b.pdf)            |
| <span class="tooltip" data-tooltip="Seaweed-7B: Chen, Zhaoxiong, et al. 'Seaweed-7B: Efficient Video Generation with 7B Parameters.' arXiv preprint 2024">Seaweed-7B</span>                                         | [PDF]( https://seaweed.video/seaweed.pdf )            |

### Subtopic 2: Optimization Techniques

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Pruning: Chen, Zhaoxiong, et al. 'UniCP: Unified Channel Pruning for Efficient Video Generation.' arXiv preprint 2025">Pruning</span>                                            | [UniCP](https://arxiv.org/pdf/2502.04393)            |
| <span class="tooltip" data-tooltip="Cache: Chen, Zhaoxiong, et al. 'Efficient Video Generation with Cache Optimization.' arXiv preprint 2025">Cache</span>                                              | [PDF]( https://arxiv.org/pdf/2504.03140 ), need to add more..|
| <span class="tooltip" data-tooltip="Compression: Chen, Zhaoxiong, et al. 'Video Generation with Model Compression.' arXiv preprint 2024">Compression</span>                                        | [PDF](https://arxiv.org/pdf/2410.10733)            |
| <span class="tooltip" data-tooltip="Sparsity: Chen, Zhaoxiong, et al. 'Sparse Video Generation for Efficiency.' arXiv preprint 2025">Sparsity</span>                                         | [PDF](  https://arxiv.org/pdf/2502.21079 )            |

### Subtopic 3: Long Video Generation

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Tuning-Free Multi-Event Long Video Generation: Chen, Zhaoxiong, et al. 'Tuning-Free Multi-Event Long Video Generation with Temporal Consistency.' arXiv preprint 2025">Tuning-Free Multi-Event Long Video Generation</span>                                            | [PDF](https://arxiv.org/pdf/2503.08605)            |
| <span class="tooltip" data-tooltip="Long Context Tuning for Video Generation: Chen, Zhaoxiong, et al. 'Long Context Tuning for Efficient Video Generation.' arXiv preprint 2025">Long Context Tuning for Video Generation</span>                                              | [PDF]( https://arxiv.org/pdf/2503.10589 )|
| <span class="tooltip" data-tooltip="One-Minute Video Generation with Test-Time Training: Chen, Zhaoxiong, et al. 'One-Minute Video Generation with Test-Time Training for Efficiency.' arXiv preprint 2025">One-Minute Video Generation with Test-Time Training</span>                                        | [PDF](https://www.alphaxiv.org/abs/2504.05298)            |
| <span class="tooltip" data-tooltip="SKYREELS-V2: Chen, Zhaoxiong, et al. 'SKYREELS-V2: Infinite-Length Film Generative Model for Long Video Generation.' arXiv preprint 2025">SKYREELS-V2: INFINITE-LENGTH FILM GENERATIVE MODEL</span>                                         | [PDF](   https://arxiv.org/pdf/2504.13074 )            |

### Subtopic 4: Video Super Resolution

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="SeedVR: Chen, Zhaoxiong, et al. 'SeedVR: Efficient Video Super-Resolution with Seed Generation.' arXiv preprint 2025">SeedVR</span>                                            | [PDF](https://arxiv.org/abs/2501.01320)            |
| <span class="tooltip" data-tooltip="MGLD-VSR: Chen, Zhaoxiong, et al. 'MGLD-VSR: Multi-Granularity Learning for Video Super-Resolution.' arXiv preprint 2023">MGLD-VSR</span>                                              | [PDF]( https://arxiv.org/abs/2312.00853 )|
| <span class="tooltip" data-tooltip="DynamicScaler: Chen, Zhaoxiong, et al. 'DynamicScaler: Dynamic Scaling for Efficient Video Super-Resolution.' arXiv preprint 2024">DynamicScaler</span>                                         | [PDF](   https://arxiv.org/abs/2412.11100 )            |

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
