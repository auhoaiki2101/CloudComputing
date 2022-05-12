# Chương 1: Giới thiệu về AWSDeepRacer
## 1.AWSDeepRacer
### 1.1 Khái Niệm
+ AWS DeepRacer là một xe đua tự hành có tỷ lệ 1/18, được thiết kế để kiểm thử các mô hình RL thông qua việc đua xe trên đường đua thực tế. Sử dụng camera để quan sát đường đua và mô hình tăng cường để điều khiển bướm ga và vô lăng, chiếc xe là minh chứng cho thấy một mô hình được huấn luyện trong môi trường giả lập có thể được triển khai sang thế giới thực.
+ AWS cung cấp mô hình trong Amazon SageMaker và đào tạo, thử nghiệm và lặp lại một cách nhanh chóng và dễ dàng trên đường đua trong trình mô phỏng đua xe AWS DeepRacer 3D.
+ Giúp người dùng nhanh chóng bắt đầu học máy với các hướng dẫn thực hành giúp tìm hiểu kiến thức cơ bản về học máy, bắt đầu đào tạo các mô hình học tập củng cố và kiểm tra chúng trong trải nghiệm đua xe ô tô tự hành, thú vị.
### 1.2 Dịch Vụ Dùng
AWS Sử dụng những services sau để hoạt động và cung cấp chức năng:
+ Amazon Simple Storage Service: Lưu trữ model.
+ AWS Lambda: Tạo và chạy những thuật toán ‘thưởng’.
+ AWS CloudFormation: Tạo chế độ cho những models chạy.
+ SageMaker: huấn luyện những models.
+ AWS RoboMaker: Tạo ra môi trường để huấn luyện và thử nghiệm.

![alt text](https://github.com/auhoaiki2101/CloudComputing/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20Thi%E1%BB%87u/Media/AWSServices.jpg)

Với những services ở trên, AWSDeepRacer giúp người dùng không cần phải bận tâm quá nhiều về việc lưu trữ, hay sử dụng những docker để tạo ra môi trường giả lập:
+ Dựa trên các container Robomaker và Sagemaker, hỗ trợ trên rất nhiều nền tảng thiết lập CPU và GPU.
+ Tập hợp rất nhiều kịch bản cho phép dễ dàng thiết kế model, không cần phải làm mọi thứ từ con số 0.
+ Cho phép các bản mẫu AWS DeepRacer từ nguồn khác; Cho phép tải lên mô hình đã được đào tạo sẵn.
Bên cạnh đó, AWSDeepRacer còn giúp đỡ trong việc xây dựng model kể cả mô phỏng lẫn vật lý:
+ AWS DeepRacer giúp xây dựng một kết nối wifi dựa phương tiện AWS và AWS DeepRacer Console.
+ AWS DeepRacer có thể chỉnh sửa một số thông tin của phương tiện (tốc độ, độ cân bằng, các góc bánh xe)
+ AWS DeepRacer cũng đưa ra một số templates để xây dựng phương tiện cũng như đường đua vật lý để thử nghiệm ngoài đời thật
AWSDeepRacer còn bảo dữ liệu người dùng ngăn chặn những xe mô phỏng của mình có thể bị rò rỉ ra ngoài:
+ Dùng xác thực đa yếu tố(MFA) với mỗi người dùng mỗi lần đăng nhập.
+ Dùng SSL/TLS để truy xuất với dữ liệu của AWS.
+ Dùng API và lưu trữ thông tin người đăng nhập bằng AWS CloudTrail.
+ Dùng các cách bảo mật mã hóa.
### 1.3 Hạn Chế
+ Vì đây là mô phỏng không thể nắm bắt chính xác tất cả các khía cạnh của thế giới thực, do đó các mô hình được đào tạo về mô phỏng có thể không hoạt động tốt trong thế giới thực. Mô phỏng như vậy thường được gọi là khoảng cách hiệu suất mô phỏng-thực (sim2real).
- Giải pháp:
+ Để giúp giảm khoảng cách hiệu suất real2sim, hãy đảm bảo sử dụng màu sắc, hình dạng và kích thước giống nhau hoặc tương tự cho cả bản nhạc mô phỏng và bản nhạc thực. Hãy sử dụng các chướng ngại vật xung quanh đường đua thực. Ngoài ra, hãy hiệu chỉnh cẩn thận phạm vi tốc độ và góc lái của xe để không gian hành động được sử dụng trong huấn luyện phù hợp với thế giới thực. Đánh giá hiệu suất mô hình trong một đường mô phỏng khác với đường đua được sử dụng trong đào tạo có thể cho thấy mức độ chênh lệch hiệu suất thực tế.

### 1.4 AWS DeepRacer Evo
+ AWS DeepRacer Evo là xe đua tự hành thế hệ mới. Chiếc xe này được trang bị đầy đủ camera stereo và cảm biến LiDAR nhằm hỗ trợ tránh chướng ngại vật và đua đối đầu trực tiếp, mang tới cho các nhà phát triển mọi thứ họ cần để đưa trải nghiệm đua lên tầm cao mới. Với các cuộc đua tránh chướng ngại vật, nhà phát triển sử dụng cảm biến để phát hiện và tránh các trước ngại vật được đặt trên đường đua. Với hình thức đối đầu trực tiếp, các nhà phát triển đua với một xe DeepRacer khác trên cùng một đường đua, cố gắng tránh xe đó mà vẫn tìm cách hoàn thành vòng đua trong thời gian ngắn nhất. Các camera nằm bên phải và bên trái ở phía trước tạo thành hệ thống camera stereo, giúp chiếc xe xác định thông tin độ sâu bằng hình ảnh. Sau đó, xe dựa vào thông tin này để cảm nhận và tránh các chướng ngại vật xuất hiện trên đường đua. Cảm biến LiDAR nằm ở phía sau, giúp phát hiện các chướng ngại vật phía sau và bên cạnh xe.
+ 
<img src="https://github.com/auhoaiki2101/CloudComputing/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20Thi%E1%BB%87u/Media/DeepRacer%20Evo%207.png" width="400">

## 2.Học Tăng Cường Reinforment Learning (RL)
### 2.1 Khái Niệm
+ Reinforment Learning là một kỹ thuật Học máy dựa trên phản hồi, trong đó tác nhân học cách cư xử trong môi trường bằng cách thực hiện các hành động và xem kết quả của các hành động. Đối với mỗi hành động tốt, người đại diện nhận được phản hồi tích cực và đối với mỗi hành động xấu, người đại diện nhận được phản hồi tiêu cực hoặc hình phạt. Giúp học các hành vi rất phức tạp mà không yêu cầu bất kỳ dữ liệu đào tạo được gắn nhãn nào và có thể đưa ra quyết định ngắn hạn trong khi tối ưu hóa cho mục tiêu dài hạn. RL là một cách tiếp cận tập trung vào việc học để hoàn thành mục tiêu bằng việc tương tác trực tiếp với môi trường.

<img src="https://github.com/auhoaiki2101/CloudComputing/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20Thi%E1%BB%87u/Media/reinforcement-learning.png" width="400">

+ RL giúp agent(ở đây là xe chúng ta muốn huấn luyện) có thể làm được task(nhiệm vụ ta giao như hoàn thành đường đua...) bằng cách đưa ra những action miễn là maxize reward (đạt được hiệu suất tối ưu).
Ví dụ: 

<img src="https://github.com/auhoaiki2101/CloudComputing/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20Thi%E1%BB%87u/Media/Reinforcement%20_Learning2.png" width="600">

- Hình ảnh trên cho thấy robot, kim cương và lửa. Mục tiêu của robot là nhận được phần thưởng là viên kim cương và tránh các chướng ngại vật được bắn ra. Robot học bằng cách thử tất cả các con đường có thể và sau đó chọn con đường mang lại cho anh ta phần thưởng với ít trở ngại nhất. Mỗi bước đúng sẽ mang lại cho robot một phần thưởng và mỗi bước sai sẽ trừ phần thưởng của robot. Tổng phần thưởng sẽ được tính khi đạt đến phần thưởng cuối cùng là kim cương.

### 2.2 Ứng Dụng Vào DeepRacer
+ Trong reinforcement learning, các mô hình AWSDeepRacer dựa theo mục tiêu được định sẵn mà sẽ tác động với môi trường đường đua để tối đa hóa phần thưởng mà mình sẽ đạt
+ Mục tiêu của RL trong AWSDeepRacer là tìm ra mô hình tối ưu nhất sau khi huấn luyện để có thể đem ra thực nghiệm ngoài thế giới vật lý.

![Alt Text](https://github.com/auhoaiki2101/CloudComputing/blob/main/Ch%C6%B0%C6%A1ng%201%20-%20Gi%E1%BB%9Bi%20Thi%E1%BB%87u/Media/DeepRacer%20.gif)

AWSDeepRacer đưa ra rất nhiều lợi ích khi huấn luyện mô hình với một môi trường mô phỏng sử dụng RL:
+ Mô phỏng có thể ước tính mức độ tiến bộ mà mô hình đã đạt được và xác định thời điểm nó đi chệch hướng để tính toán phần thưởng.
+ Mô phỏng giải phóng người huấn luyện khỏi những công việc tẻ nhạt để thiết lập lại chiếc xe mỗi khi nó đi ra khỏi đường đua, như được thực hiện trong môi trường vật lý.
+ Mô phỏng có thể tăng tốc độ đào tạo.
Mô phỏng cung cấp khả năng kiểm soát tốt hơn các điều kiện môi trường, ví dụ: chọn các tuyến đường, bối cảnh và tình trạng xe khác nhau.
