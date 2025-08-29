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
| <span class="tooltip" data-tooltip="[1]Dao, Tri, et al. 'Flashattention: Fast and memory-efficient exact attention with io-awareness.' Advances in neural information processing systems 35 (2022): 16344-16359 [2]Dao, Tri. 'FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning.' The Twelfth International Conference on Learning Representations. [3]Shah, Jay, et al. 'Flashattention-3: Fast and accurate attention with asynchrony and low-precision.' Advances in Neural Information Processing Systems 37 (2024): 68658-68685.">FlashAttention 1, 2, 3</span>             | [PDF](https://arxiv.org/pdf/2205.14135), [PDF](https://arxiv.org/pdf/2307.08691), [PDF](https://arxiv.org/pdf/2407.08608)                                                          |
| <span class="tooltip" data-tooltip="Kwon, Woosuk, et al. 'Efficient memory management for large language model serving with pagedattention.' Proceedings of the 29th symposium on operating systems principles. 2023.">PagedAttention (vLLM)</span>                | [PDF](https://arxiv.org/pdf/2309.06180)            |
| <span class="tooltip" data-tooltip="Zheng, Lianmin, et al. 'Sglang: Efficient execution of structured language model programs.' Advances in neural information processing systems 37 (2024): 62557-62583.">SGLang</span>                               | [PDF](https://arxiv.org/pdf/2312.07104)            |
| <span class="tooltip" data-tooltip="Dong, Juechu, et al. 'Flex attention: A programming model for generating optimized attention kernels.' arXiv preprint arXiv:2412.05496 (2024).' arXiv preprint 2024">FlexAttention</span>                        | [PDF](https://arxiv.org/pdf/2412.05496)            |
| <span class="tooltip" data-tooltip="Ye, Zihao, et al. 'FlashInfer: Efficient and Customizable Attention Engine for LLM Inference Serving.' Eighth Conference on Machine Learning and Systems.">FlashInfer</span>                           | [PDF](https://arxiv.org/pdf/2501.01005)            |
| <span class="tooltip" data-tooltip="Zhang, Jintao, et al. 'SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference.' Forty-second International Conference on Machine Learning.">SpargeAttention</span>                      | [PDF](https://arxiv.org/pdf/2502.18137)            |
| <span class="tooltip" data-tooltip="[1]Zhang, Jintao, et al. 'SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration.' The Thirteenth International Conference on Learning Representations. [2]Zhang, Jintao, et al. 'SageAttention2: Efficient Attention with Thorough Outlier Smoothing and Per-thread INT4 Quantization.' Forty-second International Conference on Machine Learning.">SageAttention 1,2</span>                    | [PDF](https://arxiv.org/pdf/2410.02367), [PDF](https://arxiv.org/abs/2411.10958)                                                                                      |

### Subtopic 2: Sparse Attention

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Liu, Zichang, et al. 'Deja vu: Contextual sparsity for efficient llms at inference time.' International Conference on Machine Learning. PMLR, 2023.">DejaVu</span>                               | [PDF](https://arxiv.org/pdf/2310.17157)            |
| <span class="tooltip" data-tooltip="Zhang, Zhenyu, et al. 'H2o: Heavy-hitter oracle for efficient generative inference of large language models.' Advances in Neural Information Processing Systems 36 (2023): 34661-34710.">H2O</span>                                  | [PDF](https://arxiv.org/abs/2306.14048)            |
| <span class="tooltip" data-tooltip="Wang, Hanrui, Zhekai Zhang, and Song Han. 'Spatten: Efficient sparse attention architecture with cascade token and head pruning.' 2021 IEEE International Symposium on High-Performance Computer Architecture (HPCA). IEEE, 2021.">SpAttn</span>                               | [PDF](https://arxiv.org/pdf/2012.09852)            |
| <span class="tooltip" data-tooltip="Shazeer, Noam, et al. 'Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.' arXiv preprint arXiv:1701.06538 (2017).">MoE</span>                                  | [PDF](https://arxiv.org/pdf/1701.06538)            |
| <span class="tooltip" data-tooltip="Rajbhandari, Samyam, et al. 'Deepspeed-moe: Advancing mixture-of-experts inference and training to power next-generation ai scale.' International conference on machine learning. PMLR, 2022.">Deepspeed-MoE</span>                         | [PDF](https://arxiv.org/pdf/2201.05596)            |

### Subtopic 3: Kernel Generation & Compiler

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Chen, Tianqi, et al. 'TVM: An automated End-to-End optimizing compiler for deep learning.' 13th USENIX Symposium on Operating Systems Design and Implementation (OSDI 18). 2018.">TVM</span>                                  | [PDF](https://www.usenix.org/system/files/osdi18-chen.pdf)   |
| <span class="tooltip" data-tooltip="Zheng, Lianmin, et al. 'Ansor: Generating {High-Performance} tensor programs for deep learning.' 14th USENIX symposium on operating systems design and implementation (OSDI 20). 2020.">Ansor</span>                                | [PDF](https://arxiv.org/pdf/2006.06762)            |
| <span class="tooltip" data-tooltip="Lattner, Chris, et al. 'MLIR: A compiler infrastructure for the end of Moore's law.' arXiv preprint arXiv:2002.11054 (2020).">MLIR</span>                                 | [PDF](https://arxiv.org/abs/2002.11054)            |

### Subtopic 4: Execution Optimization/Serving

| Paper                                | Link                                               |
|:--------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Zheng, Lianmin, et al. 'Alpa: Automating inter-and {Intra-Operator} parallelism for distributed deep learning.' 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22). 2022.">Alpa</span>                                 | [PDF](https://www.usenix.org/system/files/osdi22-zheng-lianmin.pdf)   |
| <span class="tooltip" data-tooltip="Yu, Gyeong-In, et al. 'Orca: A distributed serving system for Transformer-Based generative models.' 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI 22). 2022.">Orca</span>                                 | [PDF]( )            |
| <span class="tooltip" data-tooltip="Sheng, Ying, et al. 'Flexgen: High-throughput generative inference of large language models with a single gpu.' International Conference on Machine Learning. PMLR, 2023.">FlexGen</span>                              | [PDF](https://arxiv.org/pdf/2303.06865)            |
| <span class="tooltip" data-tooltip="Rajbhandari, Samyam, et al. 'Zero: Memory optimizations toward training trillion parameter models.' SC20: International Conference for High Performance Computing, Networking, Storage and Analysis. IEEE, 2020.">ZeRO-Offloading</span>                      | [PDF](https://arxiv.org/abs/1910.02054)   |
| <span class="tooltip" data-tooltip="Shoeybi, Mohammad, et al. 'Megatron-lm: Training multi-billion parameter language models using model parallelism.' arXiv preprint arXiv:1909.08053 (2019).">Megatron-LM</span>                          | [PDF](https://arxiv.org/abs/1909.08053)            |
| <span class="tooltip" data-tooltip="Hong, Ke, et al. 'Flashdecoding++: Faster large language model inference on gpus.' arXiv preprint arXiv:2311.01282 (2023).">FlashDecoding++</span>                      | [PDF](https://arxiv.org/pdf/2311.01282)            |
| <span class="tooltip" data-tooltip="Agrawal, Amey, et al. 'Taming {Throughput-Latency} tradeoff in {LLM} inference with {Sarathi-Serve}.' 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI 24). 2024.">SarathiServe</span>                         | [PDF](https://www.usenix.org/system/files/osdi24-agrawal.pdf)   |

---

## Chapter II: Efficient LLM

### Subtopic 1: LLM 101

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Vaswani, Ashish, et al. 'Attention is all you need.' Advances in neural information processing systems 30 (2017).">Attention is All You Need</span>                            | [PDF](https://arxiv.org/abs/1706.03762)            |
| <span class="tooltip" data-tooltip="Devlin, Jacob, et al. 'Bert: Pre-training of deep bidirectional transformers for language understanding.' Proceedings of the 2019 conference of the North American chapter of the association for computational linguistics: human language technologies, volume 1 (long and short papers). 2019.">BERT</span> | [PDF](https://arxiv.org/abs/1810.04805)            |
| <span class="tooltip" data-tooltip="Brown, Tom, et al. 'Language models are few-shot learners.' Advances in neural information processing systems 33 (2020): 1877-1901.">GPT-3</span>| [PDF](https://arxiv.org/abs/2005.14165)            |
| <span class="tooltip" data-tooltip="Kaplan, Jared, et al. 'Scaling laws for neural language models.' arXiv preprint arXiv:2001.08361 (2020).">Scaling Laws</span>    | [PDF](https://arxiv.org/pdf/2001.08361)            |
| <span class="tooltip" data-tooltip="Ouyang, Long, et al. 'Training language models to follow instructions with human feedback.' Advances in neural information processing systems 35 (2022): 27730-27744.">RLHF</span> | [PDF](https://arxiv.org/abs/2203.02155)            |
| <span class="tooltip" data-tooltip="[1]Schulman, John, et al. 'Proximal policy optimization algorithms.' arXiv preprint arXiv:1707.06347 (2017). [2]Rafailov, Rafael, et al. 'Direct preference optimization: Your language model is secretly a reward model.' Advances in neural information processing systems 36 (2023): 53728-53741.">PPO/DPO</span>         | [PDF](https://arxiv.org/abs/1707.06347) , [PDF](https://arxiv.org/abs/2305.18290)           |


### Subtopic 2: Efficient Inference & Long-context

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="[1]Xiao, Guangxuan, et al. 'Efficient streaming language models with attention sinks.' arXiv preprint arXiv:2309.17453 (2023).; [2]Xiao, Guangxuan, et al. 'Duoattention: Efficient long-context llm inference with retrieval and streaming heads.' arXiv preprint arXiv:2410.10819 (2024).">Streaming LLM & DuoAttention</span>                         | [PDF](https://arxiv.org/abs/2309.17453), [PDF](https://arxiv.org/pdf/2410.10819)                                                                                                      |
| <span class="tooltip" data-tooltip="Jiang, Huiqiang, et al. 'Minference 1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention.' Advances in Neural Information Processing Systems 37 (2024): 52481-52515.">MInference</span>      | [PDF](https://arxiv.org/abs/2407.02490  )          |
| <span class="tooltip" data-tooltip="Zhang, Zhenyu, et al. 'H2o: Heavy-hitter oracle for efficient generative inference of large language models.' Advances in Neural Information Processing Systems 36 (2023): 34661-34710.">H2O</span>  | [PDF](https://arxiv.org/abs/2306.14048)            |
| <span class="tooltip" data-tooltip="[1]Oren, Matanel, et al. 'Transformers are multi-state rnns.' arXiv preprint arXiv:2401.06104 (2024).[2]Liu, Zirui, et al. 'Kivi: A tuning-free asymmetric 2bit quantization for kv cache.' arXiv preprint arXiv:2402.02750 (2024).">TOVA/KIVI</span>       | [PDF](https://arxiv.org/pdf/2401.06104), [PDF](https://arxiv.org/abs/2402.02750)            |
| <span class="tooltip" data-tooltip="[1]Leviathan, Yaniv, Matan Kalman, and Yossi Matias. 'Fast inference from transformers via speculative decoding.' International Conference on Machine Learning. PMLR, 2023. [2]Cai, Tianle, et al. 'Medusa: Simple llm inference acceleration framework with multiple decoding heads.' arXiv preprint arXiv:2401.10774 (2024).">Speculative Decoding</span>                                 | [PDF](https://arxiv.org/abs/2211.17192), [PDF](https://arxiv.org/abs/2401.10774)             |
| <span class="tooltip" data-tooltip="Liu, Aixin, et al. 'Deepseek-v3 technical report.' arXiv preprint arXiv:2412.19437 (2024).">Multi-token prediction: Deepseek-v3</span>                               | [PDF](https://arxiv.org/abs/2412.19437)                                  |

### Subtopic 3: Model Compression (Quant & Pruning)

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="[1]Dettmers, Tim, et al. 'Gpt3. int8 (): 8-bit matrix multiplication for transformers at scale.' Advances in neural information processing systems 35 (2022): 30318-30332. [2]Frantar, Elias, et al. 'Gptq: Accurate post-training quantization for generative pre-trained transformers.' arXiv preprint arXiv:2210.17323 (2022).">LLM.int8()/GPTQ</span> | [PDF](https://arxiv.org/abs/2208.07339), [PDF](https://arxiv.org/abs/2210.17323)            |
| <span class="tooltip" data-tooltip="Lin, Ji, et al. 'Awq: Activation-aware weight quantization for on-device llm compression and acceleration.' Proceedings of machine learning and systems 6 (2024): 87-100.">AWQ</span>  | [PDF](https://arxiv.org/abs/2306.00978)            |
| <span class="tooltip" data-tooltip="Ma, Xinyin, Gongfan Fang, and Xinchao Wang. 'Llm-pruner: On the structural pruning of large language models.' Advances in neural information processing systems 36 (2023): 21702-21720.">LLM Pruner</span>| [PDF](https://arxiv.org/abs/2305.11627)            |
| <span class="tooltip" data-tooltip="Xia, Mengzhou, et al. 'Sheared llama: Accelerating language model pre-training via structured pruning.' arXiv preprint arXiv:2310.06694 (2023).">ShearedLlama</span>    | [PDF](https://arxiv.org/pdf/2310.06694)            |

### Subtopic 4: Efficient Training

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Rajbhandari, Samyam, et al. 'Zero: Memory optimizations toward training trillion parameter models.' SC20: International Conference for High Performance Computing, Networking, Storage and Analysis. IEEE, 2020.">ZeRO</span> | [PDF](https://arxiv.org/abs/1910.02054)  |
| <span class="tooltip" data-tooltip="Shoeybi, Mohammad, et al. 'Megatron-lm: Training multi-billion parameter language models using model parallelism.' arXiv preprint arXiv:1909.08053 (2019).">Megatron-LM</span>  | [PDF](https://arxiv.org/abs/1909.08053)            |
| <span class="tooltip" data-tooltip="[1]Hu, Edward J., et al. 'Lora: Low-rank adaptation of large language models.' ICLR 1.2 (2022): 3.[2]Dettmers, Tim, et al. 'Qlora: Efficient finetuning of quantized llms.' Advances in neural information processing systems 36 (2023): 10088-10115.">LoRA & QLoRA</span>| [PDF](https://arxiv.org/abs/2106.09685), [PDF](https://arxiv.org/abs/2305.14314)            |

### Subtopic 5: Efficient Model Designs

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="[1]Fedus, William, Barret Zoph, and Noam Shazeer. 'Switch transformers: Scaling to trillion parameter models with simple and efficient sparsity.' Journal of Machine Learning Research 23.120 (2022): 1-39. [2]Shazeer, Noam, et al. 'Outrageously large neural networks: The sparsely-gated mixture-of-experts layer.' arXiv preprint arXiv:1701.06538 (2017).">Switch Transformers/Outrageously Large Neural Networks</span> | [PDF](https://arxiv.org/abs/2101.03961), [PDF](https://arxiv.org/abs/1701.06538)  |
| <span class="tooltip" data-tooltip="Liu, Aixin, et al. 'Deepseek-v3 technical report.' arXiv preprint arXiv:2412.19437 (2024).">MLA Attention</span>  | [PDF](https://arxiv.org/abs/2412.19437)            |
| <span class="tooltip" data-tooltip="Gu, Albert, and Tri Dao. 'Mamba: Linear-time sequence modeling with selective state spaces.' arXiv preprint arXiv:2312.00752 (2023).">Mamba</span>| [PDF](https://arxiv.org/abs/2312.00752)            |


---

## Chapter III: Video Generation

### Subtopic 1: SOTA/Baseline Model

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Yang, Zhuoyi, et al. 'Cogvideox: Text-to-video diffusion models with an expert transformer.' arXiv preprint arXiv:2408.06072 (2024).">CogVideoX</span>       | [PDF](https://arxiv.org/pdf/2408.06072)            |
| <span class="tooltip" data-tooltip="Kong, Weijie, et al. 'Hunyuanvideo: A systematic framework for large video generative models.' arXiv preprint arXiv:2412.03603 (2024).">HunyuanVideo</span> | [PDF]( https://arxiv.org/pdf/2412.03603 )            |
| <span class="tooltip" data-tooltip="Wan, Team, et al. 'Wan: Open and advanced large-scale video generative models.' arXiv preprint arXiv:2503.20314 (2025).">WAN</span>| [PDF](https://files.alicdn.com/tpsservice/5c9de1c74de03972b7aa657e5a54756b.pdf)            |
| <span class="tooltip" data-tooltip="Seawead, Team, et al. 'Seaweed-7b: Cost-effective training of video generation foundation model.' arXiv preprint arXiv:2504.08685 (2025).">Seaweed-7B</span>    | [PDF]( https://seaweed.video/seaweed.pdf )            |

### Subtopic 2: Optimization Techniques

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Sun, Wenzhang, et al. 'UniCP: A Unified Caching and Pruning Framework for Efficient Video Generation.' arXiv preprint arXiv:2502.04393 (2025).">Pruning</span>       | [PDF](https://arxiv.org/pdf/2502.04393)            |
| <span class="tooltip" data-tooltip="Ma, Xuran, et al. 'Model Reveals What to Cache: Profiling-Based Feature Reuse for Video Diffusion Models.' arXiv preprint arXiv:2504.03140 (2025).">Cache</span>         | [PDF]( https://arxiv.org/pdf/2504.03140 )|
| <span class="tooltip" data-tooltip="Chen, Junyu, et al. 'Deep compression autoencoder for efficient high-resolution diffusion models.' arXiv preprint arXiv:2410.10733 (2024).">Compression</span>   | [PDF](https://arxiv.org/pdf/2410.10733)            |
| <span class="tooltip" data-tooltip="Xia, Yifei, et al. 'Training-free and adaptive sparse attention for efficient long video generation.' arXiv preprint arXiv:2502.21079 (2025).">Sparsity</span>    | [PDF](  https://arxiv.org/pdf/2502.21079 )            |

### Subtopic 3: Long Video Generation

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Kim, Subin, et al. 'Tuning-Free Multi-Event Long Video Generation via Synchronized Coupled Sampling.' arXiv preprint arXiv:2503.08605 (2025).">Tuning-Free Multi-Event Long Video Generation</span>       | [PDF](https://arxiv.org/pdf/2503.08605)            |
| <span class="tooltip" data-tooltip="Guo, Yuwei, et al. 'Long context tuning for video generation.' arXiv preprint arXiv:2503.10589 (2025).">Long Context Tuning for Video Generation</span>         | [PDF]( https://arxiv.org/pdf/2503.10589 )|
| <span class="tooltip" data-tooltip="Dalal, Karan, et al. 'One-minute video generation with test-time training.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">One-Minute Video Generation with Test-Time Training</span>   | [PDF](https://www.alphaxiv.org/abs/2504.05298)            |
| <span class="tooltip" data-tooltip="Chen, Guibin, et al. 'Skyreels-v2: Infinite-length film generative model.' arXiv preprint arXiv:2504.13074 (2025).">SKYREELS-V2</span>    | [PDF](   https://arxiv.org/pdf/2504.13074 )            |

### Subtopic 4: Video Super Resolution

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Wang, Jianyi, et al. 'Seedvr: Seeding infinity in diffusion transformer towards generic video restoration.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">SeedVR</span>       | [PDF](https://arxiv.org/abs/2501.01320)            |
| <span class="tooltip" data-tooltip="Yang, Xi, et al. 'Motion-guided latent diffusion for temporally consistent real-world video super-resolution.' European conference on computer vision. Cham: Springer Nature Switzerland, 2024.">MGLD-VSR</span>         | [PDF]( https://arxiv.org/abs/2312.00853 )|
| <span class="tooltip" data-tooltip="Liu, Jinxiu, et al. 'Dynamicscaler: Seamless and scalable video generation for panoramic scenes.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">DynamicScaler</span>    | [PDF](   https://arxiv.org/abs/2412.11100 )            |

---

## Chapter IV: Secure LLM

### Subtopic 1: Diffusion Model/Flow Matching

### Subtopic 2: Watermarking

### Subtopic 3: Efficient CNN

### Subtopic 4: Encryption

---

## Chapter V: MLLM Video Understanding

### Subtopic 1: SOTA/Baseline

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Bai, Shuai, et al. 'Qwen2. 5-vl technical report.' arXiv preprint arXiv:2502.13923 (2025).">Qwen2.5-VL</span>       | [PDF](https://arxiv.org/abs/2502.13923)            |
| <span class="tooltip" data-tooltip="Jiang, Jindong, et al. 'Token-efficient long video understanding for multimodal llms.' arXiv preprint arXiv:2503.04130 (2025).">Storm</span>         | [PDF](https://research.nvidia.com/labs/lpr/storm/) |
| <span class="tooltip" data-tooltip="Lin, Bin, et al. 'Video-llava: Learning united visual representation by alignment before projection.' arXiv preprint arXiv:2311.10122 (2023).">LLaVA</span>   | [PDF](https://arxiv.org/abs/2311.10122)            |
| <span class="tooltip" data-tooltip="Touvron, Hugo, et al. 'Llama: Open and efficient foundation language models.' arXiv preprint arXiv:2302.13971 (2023).">LLaMA</span>    | [PDF](https://arxiv.org/abs/2302.13971)            |
| <span class="tooltip" data-tooltip="Guo, Dong, et al. 'Seed1. 5-vl technical report.' arXiv preprint arXiv:2505.07062 (2025).">Seed1.5 VL</span>       | [PDF](https://arxiv.org/abs/2505.07062)            |
| <span class="tooltip" data-tooltip="Team, Kwai Keye, et al. 'Kwai Keye-VL Technical Report.' arXiv preprint arXiv:2507.01949 (2025).">Kwai Keye-VL</span>         | [PDF](https://arxiv.org/abs/2507.01949) |

### Subtopic 2: System Optimization Techniques

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Ye, Xubing, et al. 'Atp-llava: Adaptive token pruning for large vision language models.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">ATP-LLaVA: Adaptive Token Pruning</span>       | [PDF](https://arxiv.org/pdf/2412.00447)            |
| <span class="tooltip" data-tooltip="Shen, Leqi, et al. 'Fastvid: Dynamic density pruning for fast video large language models.' arXiv preprint arXiv:2503.11187 (2025).">FastVID: Dynamic Density Pruning</span>         | [PDF](https://www.arxiv.org/pdf/2503.11187) |
| <span class="tooltip" data-tooltip="Wang, Xiao, et al. 'Adaretake: Adaptive redundancy reduction to perceive longer for video-language understanding.' arXiv preprint arXiv:2503.12559 (2025).">AdaReTaKe: Token Compression</span>   | [PDF](https://arxiv.org/pdf/2503.12559)            |
| <span class="tooltip" data-tooltip="Tao, Wei, et al. 'Cocktail: Chunk-Adaptive Mixed-Precision Quantization for Long-Context LLM Inference.' 2025 Design, Automation & Test in Europe Conference (DATE). IEEE, 2025.">Cocktail: Mixed-Precision Quantization</span>    | [PDF](https://arxiv.org/pdf/2503.23294)            |
| <span class="tooltip" data-tooltip="Zhu, Jianian, et al. 'Fastcache: Optimizing multimodal llm serving through lightweight kv-cache compression framework.' arXiv preprint arXiv:2503.08461 (2025).">FastCache: KV-Cache Compression</span>       | [PDF](https://arxiv.org/pdf/2503.08461)            |

### Subtopic 3: Attention Kernel Optimization

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Chen, Feiyang, et al. 'Attentionengine: A versatile framework for efficient attention mechanisms on diverse hardware platforms.' arXiv preprint arXiv:2502.15349 (2025).">AttentionEngine</span>       | [PDF](https://arxiv.org/abs/2502.15349)            |
| <span class="tooltip" data-tooltip="Zhang, Jintao, et al. 'SpargeAttention: Accurate and Training-free Sparse Attention Accelerating Any Model Inference.' Forty-second International Conference on Machine Learning.">SpargeAttn</span>         | [PDF](https://openreview.net/forum?id=74c3Wwk8Tc) |
| <span class="tooltip" data-tooltip="Lai, Xunhao, et al. 'Flexprefill: A context-aware sparse attention mechanism for efficient long-sequence inference.' arXiv preprint arXiv:2502.20766 (2025).">FlexPrefill</span>   | [PDF](https://arxiv.org/abs/2502.20766)            |
| <span class="tooltip" data-tooltip="Jiang, Huiqiang, et al. 'Minference 1.0: Accelerating pre-filling for long-context llms via dynamic sparse attention.' Advances in Neural Information Processing Systems 37 (2024): 52481-52515.">MInference 1.0</span>    | [PDF](https://proceedings.neurips.cc/paper_files/paper/2024/hash/5dfbe6f5671e82c76841ba687a8a9ecb-Abstract-Conference.html)            |

### Subtopic 4: Algorithm Design

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Tang, Xi, et al. 'Adaptive keyframe sampling for long video understanding.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">Adaptive Keyframe Sampling</span>       | [PDF](https://arxiv.org/pdf/2502.21271)            |
| <span class="tooltip" data-tooltip="Ye, Jinhui, et al. 'Re-thinking temporal search for long-form video understanding.' Proceedings of the Computer Vision and Pattern Recognition Conference. 2025.">Re-thinking Temporal Search</span>         | [PDF](https://www.alphaxiv.org/abs/2504.02259) |
| <span class="tooltip" data-tooltip="Li, Yixuan, et al. 'Improving llm video understanding with 16 frames per second.' arXiv preprint arXiv:2503.13956 (2025).">Improving LLM Video Understanding with 16 FPS</span>   | [PDF](https://arxiv.org/pdf/2503.13956)            |

---

## Guest Lecture Materials

| Paper                                                | Link                                               |
|:------------------------------------------------------:|----------------------------------------------------|
| <span class="tooltip" data-tooltip="Dong, Juechu, et al. 'Flex attention: A programming model for generating optimized attention kernels.' arXiv preprint arXiv:2412.05496 (2024).">FlexAttention</span>       | [PDF](https://arxiv.org/pdf/2412.05496)  |
| <span class="tooltip" data-tooltip="Dong, Joy, et al. 'FlexAttention Part II: FlexAttention for Inference.' PyTorch Blog, 30 Apr. 2025, pytorch.org/blog/flexattention-for-inference/.">FlexAttention(PyTorch Blog)</span>         | [Website]( https://pytorch.org/blog/flexattention-for-inference/ )|
| <span class="tooltip" data-tooltip="Guan, Yue, et al. 'KPerfIR: Towards a Open and Compiler-centric Ecosystem for GPU Kernel Performance Tooling on Modern AI Workloads.' Proceedings of the 19th USENIX Symposium on Operating Systems Design and Implementation (OSDI '25), USENIX Association, 2025.">DynamicScaler</span>    | [PDF](https://www.usenix.org/conference/osdi25/presentation/guan)  |
| <span class="tooltip" data-tooltip="Zhao, Liangyu, et al. 'ForestColl: Throughput-Optimal Collective Communications on Heterogeneous Network Fabrics.' arXiv preprint arXiv:2402.06787 (2024).">ForestColl</span> | [PDF](https://arxiv.org/pdf/2402.06787) |
| <span class="tooltip" data-tooltip="Wang, Zhuang, et al. 'GEMINI: Fast Failure Recovery in Distributed Training with In-Memory Checkpoints.' Proceedings of the 29th Symposium on Operating Systems Principles (SOSP '23), Association for Computing Machinery, 2023, pp. 364–381. https://doi.org/10.1145/3600006.3613145.">ForestColl</span> | [PDF](https://dl.acm.org/doi/10.1145/3600006.3613145) |
