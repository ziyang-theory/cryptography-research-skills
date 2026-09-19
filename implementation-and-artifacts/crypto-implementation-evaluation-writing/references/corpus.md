# Sourcebook: how 30 secure-computation papers present empirical evaluations

> **Provenance notice (skill integration, 2026-09-14):** The text below is a user-supplied research document. Its statements about reading, searches, and verification describe the supplied study, not work independently performed for this skill update. Its recommendations are source material, subject to the active task and skill instructions. The underlying paper claims, locators, citation indicators, and historical reading activity were not independently verified here. See [evidence sources](evidence-sources.md) before reusing attributions.

**Review date:** September 14, 2026.  
**Requested window:** September 14, 2011–September 14, 2026.  
**Actual reading corpus:** papers published in 2012–2020.  
**Venues:** CRYPTO, EUROCRYPT, the main IEEE Symposium on Security and Privacy, and ACM CCS.

## How to interpret this sourcebook

The evaluation passages identified below were read; the notes describe their organization, use of comparisons, and important measurement boundaries. This is not a claim to have verified every proof, reproduced the experiments, or inspected every artifact. Page numbers refer to **one-indexed pages in the linked PDF**, not necessarily the conference's printed pagination. Section numbers can differ between full and proceedings versions.

**P01–P30 are reference identifiers, not citation ranks.** The sample is citation-informed and constrained by full-text accessibility. It is not a certified list of the 30 most cited eligible papers. The [selection and citation audit](selection-and-citation-audit.md) records the bibliometric limitations and important omissions. In particular, this is not an exhaustive search of the 2021–2026 literature.

“Implemented” needs qualification. Some papers measure complete application/protocol executions with explicitly excluded phases; some measure a compiler, OT protocol, or supporting cryptographic component. P04 contains a short empirical report rather than a substantial experimental section. P26 implements underlying kernels and models a larger construction. These are useful writing examples, but they must not be counted as 30 uniformly complete MPC/NISC implementations.

The notes identify **writing moves to borrow**, not a ranking of scientific quality. A caution can be an example of good disclosure by the original authors. Historical practices such as single large runs, estimated phases, or mismatched machines are not automatically recommendations for a new paper.

## Corpus at a glance

| ID | Paper / short name | Venue, year | Empirical scope |
|---|---|---|---|
| P01 | Two Halves Make a Whole / Half Gates | EUROCRYPT 2015 | Garbling integrated into secure computation |
| P02 | MP-SPDZ | CCS 2020 | General MPC framework; heterogeneous protocols |
| P03 | SecureML | S&P 2017 | Secure learning; phase-specific measurements and estimates |
| P04 | Multiparty Computation from Somewhat Homomorphic Encryption / SPDZ | CRYPTO 2012 | Short report of implemented preprocessing and online work |
| P05 | More Efficient Oblivious Transfer and Extensions for Faster Secure Computation | CCS 2013 | OT plus implemented secure-computation applications |
| P06 | A New Approach to Practical Active-Secure Two-Party Computation / TinyOT | CRYPTO 2012 | Active-secure 2PC prototype |
| P07 | Non-Interactive Secure Computation Based on Cut-and-Choose | EUROCRYPT 2014 | NISC prototype; not every proposed optimization implemented |
| P08 | MiniONN | CCS 2017 | Oblivious neural-network inference |
| P09 | Optimized Honest-Majority MPC for Malicious Adversaries | S&P 2017 | Malicious honest-majority MPC; selected variants |
| P10 | Authenticated Garbling and Efficient Maliciously Secure Two-Party Computation | CCS 2017 | Malicious 2PC |
| P11 | Global-Scale Secure Multiparty Computation | CCS 2017 | Distributed malicious MPC |
| P12 | Practical Secure Aggregation for Privacy-Preserving Machine Learning | CCS 2017 | Secure aggregation; weaker implemented scope than strongest protocol |
| P13 | CrypTFlow | S&P 2020 | Secure inference; distinct software and hardware-assisted settings |
| P14 | CrypTFlow2 | CCS 2020 | Secure two-party inference |
| P15 | Overdrive | EUROCRYPT 2018 | MPC preprocessing plus application evaluation |
| P16 | TinyGarble | S&P 2015 | Circuit/compiler and local garbling components |
| P17 | More Efficient Oblivious Transfer Extensions with Security for Malicious Adversaries | EUROCRYPT 2015 | OT-extension protocol, not end-to-end MPC |
| P18 | PICCO | CCS 2013 | Compiler and distributed private computation |
| P19 | ObliVM | S&P 2015 | Programming framework; measured and estimated entries distinguished |
| P20 | GraphSC | S&P 2015 | Parallel secure graph computations |
| P21 | Privacy-Preserving Ridge Regression on Hundreds of Millions of Records | S&P 2013 | Regression prototype; local timing boundary |
| P22 | Privacy-Preserving Matrix Factorization | CCS 2013 | Application prototype; selected computation phases |
| P23 | DUPLO | CCS 2017 | Malicious 2PC with configurable cut-and-choose granularity |
| P24 | Helen | S&P 2019 | Secure learning; measured online work and modeled preprocessing |
| P25 | HyCC | CCS 2018 | Hybrid-protocol compiler and executions |
| P26 | Homomorphic Secret Sharing: Optimizations and Applications | CCS 2017 | Implemented kernels; larger-construction performance modeled |
| P27 | A Framework for Constructing Fast MPC over Arithmetic Circuits… | CCS 2017 | Arithmetic honest-majority MPC implementations |
| P28 | Efficient, Constant-Round and Actively Secure MPC: Beyond the Three-Party Case | CCS 2017 | Implemented five-party variants |
| P29 | Fast Private Set Intersection from Homomorphic Encryption | CCS 2017 | Application-specific two-party secure computation |
| P30 | Practical Multi-party Private Set Intersection from Symmetric-Key Techniques | CCS 2017 | Application-specific multiparty secure computation |

## Paper-by-paper reading notes

<a id="p01"></a>
### P01 — Half gates

**Bibliography:** Samee Zahur, Mike Rosulek, and David Evans. *Two Halves Make a Whole: Reducing Data Transfer in Garbled Circuits Using Half Gates*. EUROCRYPT 2015. [Primary PDF](https://www.cs.virginia.edu/~evans/pubs/ec2015/halfgates.pdf).  
**Read:** §5, “Performance Comparison,” PDF pp. 15–16.

**How the section works:** It moves from the construction's communication advantage to integrated measurements using a shared implementation base. Its comparison connects time, communication, and energy rather than assuming that fewer ciphertexts automatically imply lower latency. The presentation also distinguishes favorable settings from a regime in which computational overhead can matter more.

**Borrow:** Explain why the theoretical saving should affect the measured workload, then test that implication. Keep the timing boundary explicit: integrated OT and output handling matter. Distinguish measured outcomes from discussion of other possible network/computation regimes.

<a id="p02"></a>
### P02 — MP-SPDZ

**Bibliography:** Marcel Keller. *MP-SPDZ: A Versatile Framework for Multi-Party Computation*. CCS 2020. [Primary PDF, university-hosted copy](https://www.acsu.buffalo.edu/~mblanton/cse715/mp-spdz.pdf). DOI: 10.1145/3372297.3417872.  
**Read:** §1.2, “Benchmarks,” PDF p. 3; Appendix A, PDF pp. 15–16.

**How the section works:** Broad framework comparisons are organized around different security settings and computational domains. Tables carry the burden of distinguishing supported configurations, timing exclusions, and estimated entries. The interpretation depends on the surrounding definitions rather than one universal winner.

**Borrow:** Use a configuration matrix before a large benchmark table. Make representation and security differences visible, and attach exclusions or extrapolation markers to the affected entries. Do not flatten field/ring choices, input-loading policies, or corruption thresholds into a single performance ranking.

<a id="p03"></a>
### P03 — SecureML

**Bibliography:** Payman Mohassel and Yupeng Zhang. *SecureML: A System for Scalable Privacy-Preserving Machine Learning*. IEEE S&P 2017. [Primary PDF](https://www.ieee-security.org/TC/SP2017/papers/466.pdf).  
**Read:** §VI, PDF pp. 11–15.

**How the section works:** The evaluation connects implementation and network setup to learning workloads, preprocessing/online costs, and approximation choices. It uses both performance and accuracy to explain design decisions, and separates some measured outcomes from estimates. The discussion includes configurations where the proposed approach remains expensive.

**Borrow:** Treat model quality and training behavior as part of the experimental contract. Report batch-size effects without confusing a faster iteration with faster convergence. Preserve trust assumptions, synthetic-data construction, and baseline provenance when interpreting application-level improvements.

<a id="p04"></a>
### P04 — SPDZ

**Bibliography:** Ivan Damgård, Valerio Pastro, Nigel P. Smart, and Sarah Zakarias. *Multiparty Computation from Somewhat Homomorphic Encryption*. CRYPTO 2012. [Primary PDF](https://link.springer.com/content/pdf/10.1007/978-3-642-32009-5_38.pdf).  
**Read:** “Performance in Practice,” PDF p. 4.

**How the passage works:** A short empirical report establishes that preprocessing and online computation were implemented, states a concrete setting, and expresses costs in an amortized unit. Further implementation detail is delegated to companion work.

**Borrow:** Even a theory-heavy paper can connect its construction to concrete costs with clear units and a phase distinction. **Exception:** this is not a full experimental-section exemplar. Its inclusion documents practical implementation evidence; a new substantial performance claim should provide more methodological detail than this brief passage alone.

<a id="p05"></a>
### P05 — OT optimization connected to applications

**Bibliography:** Gilad Asharov, Yehuda Lindell, Thomas Schneider, and Michael Zohner. *More Efficient Oblivious Transfer and Extensions for Faster Secure Computation*. CCS 2013. [Primary PDF](https://encrypto.de/papers/ALSZ13.pdf). DOI: 10.1145/2508859.2516738.  
**Read:** §6, “Experimental Evaluation,” and §7, “Application Scenarios,” PDF pp. 9–11.

**How the section works:** An optimization ladder explains improvements to the primitive before integrated secure-computation applications show their consequence. Network settings and startup costs are separated, and application structure explains why OT improvements have different effects.

**Borrow:** Use “primitive → integration → explanation” rather than stopping at operations per second. Compare within a controlled implementation when isolating an optimization. An input-heavy workload and a gate-heavy workload need not inherit the same improvement from a faster input-transfer mechanism.

<a id="p06"></a>
### P06 — TinyOT

**Bibliography:** Jesper Buus Nielsen, Peter Sebastian Nordholt, Claudio Orlandi, and Sai Sheshank Burra. *A New Approach to Practical Active-Secure Two-Party Computation*. CRYPTO 2012. [Primary full-version PDF](https://arxiv.org/pdf/1202.3052).  
**Read:** §7, “Experimental Results,” PDF pp. 19–20.

**How the section works:** A proof-of-concept implementation is evaluated through parallel operations and a recognizable circuit workload. The presentation identifies the implementation environment, security parameters, and preprocessing treatment, allowing the reader to connect throughput to practical execution costs.

**Borrow:** Separate startup from steady-state work and state whether preprocessing is stored and later consumed. Do not silently drop base-OT cost. Some large configurations received fewer repetitions; treat that as a limitation to disclose, not a statistical practice to copy into a new evaluation.

<a id="p07"></a>
### P07 — Cut-and-choose NISC

**Bibliography:** Arash Afshar, Payman Mohassel, Benny Pinkas, and Ben Riva. *Non-Interactive Secure Computation Based on Cut-and-Choose*. EUROCRYPT 2014. [Primary PDF](https://link.springer.com/content/pdf/10.1007/978-3-642-55220-5_22.pdf).  
**Read:** §6, “Evaluation,” PDF pp. 15–17. Text read; the page-image retrieval failed.

**How the section works:** The prototype is organized around asynchronous roles: initial preparation/message, the other party's response, and final local processing. Implementation choices and the fact that a proposed optimization was not implemented are disclosed.

**Borrow:** Match the evaluation structure to the NISC interface instead of forcing it into an ordinary interactive-runtime table. State which work can be reused and under which conditions. File-mediated execution and local cycle measurements must not be described as measured network-delivery latency.

<a id="p08"></a>
### P08 — MiniONN

**Bibliography:** Jian Liu, Mika Juuti, Yao Lu, and N. Asokan. *Oblivious Neural Network Predictions via MiniONN Transformations*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p619-liuA.pdf). DOI: 10.1145/3133956.3134056.  
**Read:** §6, “Performance Evaluation,” and §7, “Complexity, Accuracy, and Overhead,” PDF pp. 8–11.

**How the section works:** Network-model examples and component costs are combined with comparisons against prior secure inference. The discussion distinguishes latency from batching benefits and treats approximation/accuracy as part of the system tradeoff. Some tabulated comparisons are estimates rather than direct executions.

**Borrow:** Make throughput and single-query latency separate claims. Use identical model semantics when asserting a direct improvement. Mark measured and estimated entries visibly, and explain expensive cases rather than selecting only a favorable neural-network architecture.

<a id="p09"></a>
### P09 — Optimized honest-majority MPC

**Bibliography:** Toshinori Araki et al. *Optimized Honest-Majority MPC for Malicious Adversaries—Breaking the 1 Billion-Gate Per Second Barrier*. IEEE S&P 2017. [Primary PDF](https://www.ieee-security.org/TC/SP2017/papers/96.pdf).  
**Read:** §IV, “Implementation and Experimentation,” PDF pp. 14–15.

**How the section works:** Low-level implementation decisions are connected to a high-throughput protocol architecture. The presentation explains the roles of pipelining, computation, and network resources, while identifying which proposed protocol variants were actually implemented.

**Borrow:** Explain an optimization through the bottleneck it changes. Separate a throughput-oriented pipeline from an online-latency objective: their preferred parameters need not coincide. A useful implementation paragraph identifies layout, vectorization, or scheduling choices only when they help explain measured behavior, not as an undifferentiated engineering inventory.

<a id="p10"></a>
### P10 — Authenticated garbling

**Bibliography:** Xiao Wang, Samuel Ranellucci, and Jonathan Katz. *Authenticated Garbling and Efficient Maliciously Secure Two-Party Computation*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p21-wangA.pdf).  
**Read:** §8, “Evaluation,” PDF pp. 11–14 in this version.

**How the section works:** Setup precedes single-execution and amortized comparisons; input/output sensitivity and communication then explain the improvement. Large and small workloads expose different fixed-cost effects. The communication comparison identifies its direction rather than implicitly claiming an aggregate total.

**Borrow:** Use a phase-aware comparison, then vary inputs, outputs, and gates to explain which component dominates. Distinguish parallel executions from repeated sequential requests. Excluded setup is still disclosed, and one-direction communication must not be reused as both-direction traffic.

<a id="p11"></a>
### P11 — Global-scale MPC

**Bibliography:** Xiao Wang, Samuel Ranellucci, and Jonathan Katz. *Global-Scale Secure Multiparty Computation*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p39-wangA.pdf).  
**Read:** §6, “Evaluation,” PDF pp. 10–13.

**How the section works:** The experiments progress through local, wide-area, and many-participant deployments. Changes in topology and geography are used to interpret irregular scaling, and comparisons acknowledge differences in guarantees or experimental conditions.

**Borrow:** Describe the actual deployment behind each party count. A timing jump when a distant region joins is not automatically evidence of worse asymptotic party complexity. State whether communication is total traffic or the maximum sent by one party, and distinguish measured baselines from values imported from other environments.

<a id="p12"></a>
### P12 — Secure aggregation

**Bibliography:** Keith Bonawitz et al. *Practical Secure Aggregation for Privacy-Preserving Machine Learning*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p1175-bonawitzA.pdf). DOI: 10.1145/3133956.3133982.  
**Read:** §7, “Evaluation,” PDF pp. 10–13.

**How the section works:** Analytical costs lead into client/server measurements and dropout-sensitive behavior. The presentation distinguishes local experiments from wide-area runs and reports aspects of its repetition and exclusion procedure.

**Borrow:** Connect failure/dropout behavior to the protocol's intended deployment. **Critical boundary:** the implemented prototype omits mechanisms associated with the stronger protocol, so its timings do not establish complete malicious-security overhead. Network experiments also change some data settings. Disclosed outlier removal is not a reason to recommend post-hoc deletion of slow runs.

<a id="p13"></a>
### P13 — CrypTFlow

**Bibliography:** Nishant Kumar et al. *CrypTFlow: Secure TensorFlow Inference*. IEEE S&P 2020. [Primary full-version PDF](https://arxiv.org/pdf/1909.07814).  
**Read:** §VI, “Experiments,” PDF pp. 10–12.

**How the section works:** The section announces its evaluation goals, presents large application results, compares matched prior workloads, and then studies components and a hardware-assisted setting. Compilation, numerical behavior, and memory-related costs help explain system results.

**Borrow:** A short roadmap can keep an application evaluation from becoming disconnected benchmark subsections. Keep the assumptions of software-only and hardware-assisted variants explicit. Use component and memory analyses to explain large-model behavior rather than presenting only a model-by-model latency table.

<a id="p14"></a>
### P14 — CrypTFlow2

**Bibliography:** Deevashwer Rathee et al. *CrypTFlow2: Practical 2-Party Secure Inference*. CCS 2020. [Primary full-version PDF](https://arxiv.org/pdf/2010.06457). DOI: 10.1145/3372297.3417274.  
**Read:** §6, “Implementation,” and §7, “Experiments,” PDF pp. 10–13.

**How the section works:** Implementation details establish faithful fixed-point behavior and cryptographic choices. Experiments move from nonlinear-operation microbenchmarks to matched model comparisons and larger inference tasks. Parameter choices and backend tradeoffs are interpreted against network and precision settings.

**Borrow:** Say which objective a parameter optimizes: minimum bytes and minimum time can select different values. Tie microbenchmarks to whole-task effects. Accuracy/precision tuning and different network regimes should be visible in the comparison contract, not silently absorbed into a headline speedup.

<a id="p15"></a>
### P15 — Overdrive

**Bibliography:** Marcel Keller, Valerio Pastro, and Dragos Rotaru. *Overdrive: Making SPDZ Great Again*. EUROCRYPT 2018. [Primary PDF](https://link.springer.com/content/pdf/10.1007/978-3-319-78372-7_6.pdf).  
**Read:** §5, “Implementation,” including §5.1, PDF pp. 24–28.

**How the section works:** The section distinguishes improvements to an older implementation from the benefit of the proposed constructions. Domain and network comparisons precede an application study with phase-level costs, and the presentation acknowledges resource limits and settings with weaker results.

**Borrow:** Include an engineering-improved old baseline when isolating protocol novelty. Keep analytic network bounds separate from observed runtime. Use the application as a check on whether preprocessing gains survive integration, and specify the direction of reported communication.

<a id="p16"></a>
### P16 — TinyGarble

**Bibliography:** Ebrahim M. Songhori et al. *TinyGarble: Highly Compressed and Scalable Sequential Garbled Circuits*. IEEE S&P 2015. [Primary PDF](https://encrypto.de/papers/SHSSK15.pdf). DOI: 10.1109/SP.2015.32.  
**Read:** §VII, “Evaluation,” PDF pp. 9–14; Appendix A was not part of this reading.

**How the section works:** Circuit metrics, compilation approaches, sequential folding, and local garbling measurements are combined to explain gains from hardware-synthesis techniques. The paper separates environments used for different implementation tasks.

**Borrow:** Report structural proxies and measured time as different kinds of evidence. Gate count, a derived transfer metric, and local garbling cycles are not measured end-to-end 2PC latency. Explain tradeoffs from folding or circuit representation rather than claiming that a smaller circuit unconditionally produces a faster complete protocol.

<a id="p17"></a>
### P17 — Malicious OT extension

**Bibliography:** Gilad Asharov, Yehuda Lindell, Thomas Schneider, and Michael Zohner. *More Efficient Oblivious Transfer Extensions with Security for Malicious Adversaries*. EUROCRYPT 2015. [Primary PDF](https://encrypto.de/papers/ALSZ15.pdf). DOI: 10.1007/978-3-662-46800-5_26.  
**Read:** §4, “Performance Evaluation,” PDF pp. 22–25.

**How the section works:** A shared implementation base supports comparisons among security settings and parameter choices. Local and wide-area measurements show the effect of startup, batching, and tradeoffs between base transfers and checks.

**Borrow:** Parameter sweeps should explain the objective and why the optimum changes with the environment. Label the implemented OT interface precisely: a random-OT benchmark does not automatically measure chosen-message OT or a complete secure-computation application. Keep security-setting comparisons stratified rather than treating weaker guarantees as an interchangeable baseline.

<a id="p18"></a>
### P18 — PICCO

**Bibliography:** Yihua Zhang, Aaron Steele, and Marina Blanton. *PICCO: A General-Purpose Compiler for Private Distributed Computation*. CCS 2013. [Primary PDF, university-hosted copy](https://www.acsu.buffalo.edu/~mblanton/cse715/picco.pdf). DOI: 10.1145/2508859.2516752.  
**Read:** §5, “Performance Evaluation,” PDF pp. 9–12.

**How the section works:** Workload examples and program variants explain compiler optimizations before scaling and external comparisons. Representation sizes and differing network environments are part of the setup. Discrepancies with a baseline implementation are discussed rather than silently ignored.

**Borrow:** Distinguish batching in a program from actual parallel CPU execution. Explain exactly what a reported time aggregates: an average across parties is not the protocol's critical-path completion time. Functional comparisons with a differently configured system do not isolate security or protocol efficiency.

<a id="p19"></a>
### P19 — ObliVM

**Bibliography:** Chang Liu, Xiao Shaun Wang, Kartik Nayak, Yan Huang, and Elaine Shi. *ObliVM: A Programming Framework for Secure Computation*. IEEE S&P 2015. [Primary PDF](https://elaineshi.com/docs/oblivm.pdf).  
**Read:** §VII, “Evaluation,” PDF pp. 12–16.

**How the section works:** Progressive baselines separate compiler, ORAM, and backend effects. Structural measures and runtime play different roles; tables distinguish actual executions from estimates. Handwritten implementations provide context for generated code.

**Borrow:** Use a comparison ladder to attribute improvements, and disclose input-loading/setup exclusions. Avoid turning backend speedups on different machines into a controlled compiler claim. An author's development-time anecdote is not a user study. Do not copy mixed measured/estimated tables without preserving their visual provenance markers.

<a id="p20"></a>
### P20 — GraphSC

**Bibliography:** Kartik Nayak et al. *GraphSC: Parallel Secure Computation Made Easy*. IEEE S&P 2015. [Primary PDF](https://elaineshi.com/docs/graphsc.pdf).  
**Read:** §V, “Evaluation,” PDF pp. 11–16.

**How the section works:** Parallelism, input scale, operation counts, traffic, accuracy, and profiling form a layered argument for large graph workloads. A second deployment exposes the effect of available network capacity. Measured large-instance work is distinguished from a longer projected execution.

**Borrow:** Separate processors per server from the number of logical MPC parties. Keep total work and elapsed time distinct when evaluating parallelism. A measured iteration does not establish a measured full job, and deployments with different hardware do not form a clean network-only comparison.

<a id="p21"></a>
### P21 — Ridge regression

**Bibliography:** Valeria Nikolaenko et al. *Privacy-Preserving Ridge Regression on Hundreds of Millions of Records*. IEEE S&P 2013. [Primary PDF](https://marcjoye.github.io/papers/NWIJTB13garbled.pdf). DOI: 10.1109/SP.2013.30.  
**Read:** implementation/numerical details around PDF p. 10 and §VI, “Experiments,” PDF pp. 10–13.

**How the section works:** Synthetic experiments control problem size and numerical difficulty, phase profiles explain cost, and real data connect precision to regression quality. Comparisons to prior methods include published or projected information rather than only matched reruns.

**Borrow:** Choose workload dimensions that explain both cost and numerical correctness. Preserve the timing boundary: protocol roles run locally on one physical machine and user preparation is outside the timed computation. Numerical validation and a local performance experiment support different claims.

<a id="p22"></a>
### P22 — Matrix factorization

**Bibliography:** Valeria Nikolaenko et al. *Privacy-Preserving Matrix Factorization*. CCS 2013. [Primary PDF](https://marcjoye.github.io/papers/NIWJTB13sorting.pdf).  
**Read:** §5, “Implementation,” PDF pp. 7–8; §6, “Experiments,” PDF pp. 8–9.

**How the section works:** Engineering choices precede validation of fixed-point numerical behavior. Synthetic scaling and phase-stacked costs identify the relative work of gradient computation and sorting, with real-data experiments providing application context.

**Borrow:** Make the scope of every dataset claim explicit. Accuracy validation on a full dataset and timing a small real-data subset are not the same experiment. Costs of selected garbling/evaluation phases exclude other lifecycle work; larger distributed deployment is a prospect, not a measured outcome.

<a id="p23"></a>
### P23 — DUPLO

**Bibliography:** Vladimir Kolesnikov, Jesper Buus Nielsen, Mike Rosulek, Ni Trieu, and Roberto Trifiletti. *DUPLO: Unifying Cut-and-Choose for Garbled Circuits*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p3-kolesnikovA.pdf).  
**Read:** implementation material around PDF p. 8 and §7, “Performance,” PDF pp. 8–12.

**How the section works:** A hypothesis about component granularity motivates controlled benchmarks, followed by real circuits that reveal exceptions. Single-thread comparisons isolate relative effects; multithread measurements demonstrate achievable performance. Phase and batching tables support comparisons with earlier implementations.

**Borrow:** Let data qualify the motivating hypothesis. Disclose setup differences and unexplained baseline behavior instead of forcing a causal story. Treat one-direction communication, online cost, and total cost as separate metrics, and keep unavailable configurations distinct from resource failures.

<a id="p24"></a>
### P24 — Helen

**Bibliography:** Wenting Zheng, Raluca Ada Popa, Joseph E. Gonzalez, and Ion Stoica. *Helen: Maliciously Secure Coopetitive Learning for Linear Models*. IEEE S&P 2019. [Primary extended-version PDF](https://arxiv.org/pdf/1907.07212).  
**Read:** §8, “Evaluation,” PDF pp. 17–21.

**How the section works:** The evaluation connects theoretical scaling expectations to synthetic workloads, party-count experiments, real tasks, and accuracy. The discussion explains baseline bottlenecks and separates selected measured execution costs from preprocessing and larger-case estimates.

**Borrow:** Mark estimates even when they use measured primitive throughput. State unmeasured key setup and baseline extrapolation. Input preparation can include substantial input-dependent work; calling it preprocessing does not justify classifying it as input-independent. A hypothetical baseline bound should remain visibly different from an actual baseline run.

<a id="p25"></a>
### P25 — HyCC

**Bibliography:** Niklas Büscher, Daniel Demmler, Stefan Katzenbeisser, David Kretzmer, and Thomas Schneider. *HyCC: Compilation of Hybrid Protocols for Practical Secure Computation*. CCS 2018. [Primary PDF](https://encrypto.de/papers/BDKKS18.pdf). DOI: 10.1145/3243734.3243786.  
**Read:** cost-model validation around PDF p. 11 and §5, “Benchmarks,” PDF pp. 11–14.

**How the section works:** Predicted and observed costs validate protocol selection before application comparisons. Compiler/search costs and secure execution are separated; network and phase boundaries explain why different protocol mixtures win.

**Borrow:** Validate the model before reporting decisions based on it. Frame a general compiler's goal as useful automatic performance rather than beating every specialized implementation. Missing optimization support and setup-cost differences are material explanations, not footnotes to ignore when comparing mixed-protocol systems.

<a id="p26"></a>
### P26 — HSS optimizations

**Bibliography:** Elette Boyle, Geoffroy Couteau, Niv Gilboa, Yuval Ishai, and Michele Orrù. *Homomorphic Secret Sharing: Optimizations and Applications*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p2105-boyleA.pdf). DOI: 10.1145/3133956.3134107.  
**Read:** §6, “Concrete Efficiency,” PDF pp. 16–17.

**How the section works:** Concrete assumptions, error targets, memory, and implemented low-level kernels support a larger cost analysis. Plots for the larger construction are obtained from measured ingredients rather than a complete application execution.

**Borrow:** This is a model for carefully labeled concrete estimation, not end-to-end MPC measurement. Keep kernel measurements, modeled construction costs, and unimplemented applications separate. When reusing the presentation style, obtain current parameters independently rather than inheriting the historical security level or assumptions.

<a id="p27"></a>
### P27 — Arithmetic honest-majority MPC framework

**Bibliography:** Yehuda Lindell and Ariel Nof. *A Framework for Constructing Fast MPC over Arithmetic Circuits with Malicious Adversaries and an Honest-Majority*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p259-lindellA.pdf).  
**Read:** §7, “Experimental Results,” PDF pp. 15–16.

**How the section works:** Multiple instantiated protocol variants are compared on controlled arithmetic workloads. Party count and field choice explain when a different variant becomes preferable. The text also specifies which framework combinations were not implemented.

**Borrow:** An instantiated-variant matrix is valuable when a theorem admits many constructions. Keep field-dependent checks and security targets comparable. A fixed-depth experiment does not demonstrate a depth-scaling claim, and a back-of-the-envelope translation from Boolean results is not a measured arithmetic baseline.

<a id="p28"></a>
### P28 — Beyond three parties

**Bibliography:** Nishanth Chandran, Juan Garay, Payman Mohassel, and Satyanarayana Vusirikala. *Efficient, Constant-Round and Actively Secure MPC: Beyond the Three-Party Case*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p277-chandranA.pdf).  
**Read:** §6, “Implementation and Experiments,” PDF pp. 10–12.

**How the section works:** Implemented five-party variants are compared across deployments, with offline/online and CPU/wall-clock costs distinguished. Communication savings are related to different local and wide-area behavior, and role-specific work helps explain outcomes.

**Borrow:** State which instance of a general theorem the prototype actually evaluates. Explain incomparable security guarantees in baseline comparisons. Lower communication can coincide with worse local latency, so show the crossover rather than equating byte reduction with universal speed. Summed CPU seconds are not elapsed protocol time.

<a id="p29"></a>
### P29 — Homomorphic-encryption PSI

**Bibliography:** Hao Chen, Kim Laine, and Peter Rindal. *Fast Private Set Intersection from Homomorphic Encryption*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p1243-chenA.pdf).  
**Read:** §6, “Implementation and Performance,” PDF pp. 8–12.

**How the section works:** Parameter tables establish the application and cryptographic setting before asymmetric workload, thread, communication, and network comparisons. Sender and receiver costs are distinguished, and preparation is treated separately from the online interaction.

**Borrow:** Match set sizes, item widths, security assumptions, and resource allocation before claiming a PSI improvement. Explain why the resource budget is asymmetric. Input-dependent preprocessing is not automatically reusable, and a theoretically derived baseline communication value must not be presented as observed wire traffic.

<a id="p30"></a>
### P30 — Symmetric-key multiparty PSI

**Bibliography:** Vladimir Kolesnikov, Naor Matania, Benny Pinkas, Mike Rosulek, and Ni Trieu. *Practical Multi-party Private Set Intersection from Symmetric-Key Techniques*. CCS 2017. [Primary PDF](https://acmccs.github.io/papers/p1257-kolesnikovA.pdf).  
**Read:** §7, “Implementation and Performance,” PDF pp. 11–13.

**How the section works:** A primitive-variant comparison motivates the chosen implementation, followed by sweeps over party count, threshold, and set size. Security variants and online/total costs are separated, while thread policies and communication conventions determine the meaning of scaling results.

**Borrow:** Declare how computational resources grow with the number of parties. Label client-side traffic rather than calling it aggregate MPC communication. Improve ambiguous failure symbols by distinguishing timeout from memory exhaustion. This is a specialized secure-computation example, not a generic circuit benchmark.

## Synthesis: writing structures worth reusing

The following are qualitative patterns, not frequency counts across a systematically coded sample.

| Writing problem | Useful structure | Starting examples |
|---|---|---|
| Turning a primitive improvement into a system claim | Optimization ladder → component benchmark → integrated workload → remaining bottleneck | P05, P01 |
| Supporting a malicious-2PC improvement | Security/implementation scope → phase ledger → matched total and online comparisons → input/output/gate sensitivity | P10, P23 |
| Reporting NISC or asynchronous computation | Setup definition → role/message ledger → local work and bytes → reuse conditions | P07 |
| Separating theory from engineering | Improved old implementation → new construction → controlled difference → application consequence | P15 |
| Comparing a broad framework | Configuration/guarantee matrix → common workload → explicit unsupported and estimated cells | P02, P27 |
| Evaluating a compiler | Structural effects → cost-model validation → compile/search cost → actual execution → limitations | P19, P25 |
| Demonstrating deployment-scale behavior | Local control → distributed deployment → topology/resource explanation → limit | P11, P20, P28 |
| Establishing application usefulness | Semantics and quality target → representative workload → complete-task cost → phase profile → quality/cost tradeoff | P03, P13, P21 |
| Presenting concrete estimates honestly | Measured kernels → declared model and parameters → predicted cost → validation or explicit unimplemented boundary | P26, P24 |

### Recommended reading route for writing a new MPC/NISC section

Start with **P10** for comparison structure, **P15** for baseline fairness, and **P07** for NISC-specific accounting. Add **P23** for ablations and negative results, **P02** for security/representation stratification, and **P25** for validating models rather than trusting cost predictions. Application authors should also read **P03** or **P21** for the interaction between task quality and cost.

This route prioritizes relevance to the writing task, not citation rank. The resulting section should copy the *logic of the empirical argument*, not the papers' wording or their historical parameter choices.
