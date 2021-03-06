# EnlightenGAN-inference

Very minimalistic wrapper for [EnlightenGAN](https://github.com/VITA-Group/EnlightenGAN) inference. 
It uses carefully converted pretrained weights (+ baked in preprocessing) from the original repo and only requires `onnxruntime` as inference engine.   

## Installation

`pip install git+https://github.com/arsenyinfo/EnlightenGAN-inference`

## Usage

```python
from enlighten_inference import EnlightenOnnxModel
import cv2

img = cv2.imread('/path/to/image.jpg')
model = EnlightenOnnxModel()

processed = model.predict(img)
``` 
## Test result
1. src1
<img src="https://user-images.githubusercontent.com/49335804/127775900-3ee735fb-4274-4712-91b2-c0d89455651f.jpg" width="50%" height="50%"/>


2. dst1
<img width="281" alt="dst1_screenshot_01 08 2021" src="https://user-images.githubusercontent.com/49335804/127775794-b7448be5-3aa0-4df1-af0f-94905b49f1bf.png">


3. src2
<img src="https://user-images.githubusercontent.com/49335804/127775935-687a12b9-29ea-433d-83b9-24c1a5135f98.jpg" width="50%" height="50%"/>


4. dst2
<img width="665" alt="dst2_screenshot_01 08 2021" src="https://user-images.githubusercontent.com/49335804/127775840-550d5756-25da-4a09-ad7b-19a4c2a5cb65.png">


5. src3
<img src="https://user-images.githubusercontent.com/49335804/127788654-23a9e210-f551-4857-888f-af877cd5d46d.jpg" width="50%" height="50%"/>

6. dst3
<img width="281" alt="dst3_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127788800-965e372c-5d78-4af2-9cfb-f635e7147885.png">


7. src4
<img src="https://user-images.githubusercontent.com/49335804/127788823-71289cd5-fe91-44de-8d35-3f9deef9d150.jpg" width="50%" height="50%"/>


8. dst4
<img width="262" alt="크기변환 dst4_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127788906-235137ad-b669-4314-ab68-d0cc3e0f9431.png">

9. src5
<img src="https://user-images.githubusercontent.com/49335804/127862804-d71acb61-e8e1-497b-adc6-b5c677f78de4.jpg" width="50%" height="50%"/>

10. dst5
<img width="665" alt="dst5_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127862634-10b19c19-92ba-46ff-b62c-34e0025ec3e0.png">

11. src6
<img src="https://user-images.githubusercontent.com/49335804/127862887-e91d2501-4465-4262-83bf-507d2dbd92af.jpg" width="50%" height="50%"/>

12. dst6
<img width="665" alt="dst6_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127863057-0ad4a29d-f8f4-4f80-98de-8e9b4a4236af.png">


13. src7
<img src="https://user-images.githubusercontent.com/49335804/127862962-b003dd16-64a7-4f46-afd7-b901e037f5d5.jpg" width="50%" height="50%"/>

14. dst7
<img width="374" alt="dst7_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127863138-6aab02a5-7708-4623-8565-16f5cf500f98.png">

15. src8
<img src="https://user-images.githubusercontent.com/49335804/127866902-0ee2f04f-4731-45c3-bfda-16545c6e0fca.jpg" width="50%" height="50%"/>

16. dst8
<img width="665" alt="dst8_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127867064-58081221-f9ad-44d3-b974-2005a0cc23b0.png">

17. src9
<img src="https://user-images.githubusercontent.com/49335804/127866997-39175f32-36d6-4422-94d3-927f092c7582.jpg" width="50%" height="50%"/>

18. dst9
<img width="665" alt="dst9_screenshot_02 08 2021" src="https://user-images.githubusercontent.com/49335804/127867100-2cbfddc1-4bb3-4c47-8a89-5d4288beb056.png">

19. src10
<img src="https://user-images.githubusercontent.com/49335804/128027254-ee47a56c-fe62-4dc0-bddf-3c6b5f921f24.jpg" width="50%" height="50%"/>

20. dst10
<img width="665" alt="dst10_screenshot_03 08 2021" src="https://user-images.githubusercontent.com/49335804/128027482-e886cd0c-fe72-4ab4-84d6-981f61f8975d.png">


21. src11
<img src="https://user-images.githubusercontent.com/49335804/128027405-10a3b008-210e-4a43-b294-5bf484980c12.jpg" width="50%" height="50%"/>

22. dst11
<img width="1000" alt="크기변환 dst11_screenshot_03 08 2021" src="https://user-images.githubusercontent.com/49335804/128027969-2a058ae3-68e0-4369-a892-a6f0871214c3.png">  

23. src12
<img src="https://user-images.githubusercontent.com/49335804/128901028-6a7260c1-f177-4a8a-a49a-83019b1303de.jpg" width="50%" height="50%"/>  

24. dst12
<img width="665" alt="dst12_screenshot_11 08 2021" src="https://user-images.githubusercontent.com/49335804/128902075-dab3a8b1-ef24-4528-939a-91d32104a97c.png">
  

25. src13
<img src="https://user-images.githubusercontent.com/49335804/128901189-172638af-83a2-490d-90b2-39c22d90aa8f.jpg" width="50%" height="50%"/>    

26. dst13
<img width="374" alt="dst13_screenshot_11 08 2021" src="https://user-images.githubusercontent.com/49335804/128901378-39cb06df-ca36-4db6-ad0f-818b5ee33bd3.png">  


27. src14
<img src="https://user-images.githubusercontent.com/49335804/128904649-0d1a27f5-bc1d-4ff2-888e-bf1d11599813.jpg" width="50%" height="50%"/>    

28. dst14
<img width="281" alt="dst14_screenshot_11 08 2021" src="https://user-images.githubusercontent.com/49335804/128904884-4bddcbba-f062-4303-b785-e41d6ec14180.png">  

29. src15
<img src="https://user-images.githubusercontent.com/49335804/128904782-b2a9e499-48ab-43b8-8962-c932d5db2530.jpg" width="50%" height="50%"/>    

30. dst15
<img width="887" alt="dst15_screenshot_11 08 2021" src="https://user-images.githubusercontent.com/49335804/128904962-75290371-7d4c-4bcb-95a3-eba090fa9dca.png">  


