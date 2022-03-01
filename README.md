# KorNLI, DACON

*Contributor : Junha Park, Hongsun Jang, Jinho Jeong*, YBIGTA
<img src = "./PDF/README-1.jpg"></img>
<img src = "./PDF/README-2.jpg"></img>

### Result
<p>
The table below describes the performance of vanilla model, <br/>
without any augmentation, loss function customization, and ensemble. <br/> Learning rate are benchmarked from BERT paper and epoch is limited to 10, <br/> due to restricted GPU environment. <br/>
</p>

|Model|Vanilla Public Score|
|---|---|
|KoELECTRA|0.866|
|ROBERTa base|0.861|
|ROBERTa large|0.875|
|Ensemble|0.886|