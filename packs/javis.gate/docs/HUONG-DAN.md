# Gói `javis.gate` - SenOS Gate

Cổng cho **ChatGPT, Claude và AI khác** làm việc cùng SenOS. Bạn chat trên chatgpt.com hay claude.ai bằng gói của mình, và AI đó gọi sang SenOS khi cần: xem số liệu, đọc brain, tạo nhắc lịch, gửi Zalo...

Điểm mới từ bản 2.0.0: AI đó **đọc được hội thoại của SenOS và nhắn thẳng vào khung chat** như bạn gõ. Ví dụ:

> "Đọc hội thoại Viết Web trên SenOS rồi tư vấn anh nên làm gì tiếp."

AI đọc, tư vấn cho bạn. Bạn đồng ý ngay trên ChatGPT (hay Claude), nó nhắn vào đúng hội thoại "Viết Web" để SenOS làm tiếp. Trên SenOS bạn thấy tin đó với nhãn **từ ChatGPT**, thấy SenOS trả lời từng chữ, bấm **Dừng** được, và SenOS nhớ lại cho lần sau.

Điểm mới từ bản 2.2.0 (cần SenOS bản mới, xem mục "Đổi model và effort"):

- **Đổi model và effort ngay trong câu lệnh.** "Bảo SenOS làm việc này bằng Opus, effort cao."
- **SenOS xong việc mà ChatGPT đã thôi chờ thì chuông SenOS báo về điện thoại.** Bạn nhắn ChatGPT một câu "xem kết quả SenOS" là nó đọc được, kể cả ở một cuộc chat mới.
- **Không chỉ ChatGPT và Claude.** Gemini CLI, Codex, Cursor, Le Chat, Copilot, n8n hay script của bạn đều nối được (Bước 2c), và có đủ mọi thứ ở trên: đổi model, effort, chuông báo, đọc kết quả.

> Tiền thân là gói **SenOS trong ChatGPT** (`javis.javis-trong-chatgpt`). Máy đang cài gói cũ thấy SenOS Gate như một bản cập nhật: token, mức quyền và địa chỉ đã dán vào ChatGPT được giữ nguyên, không phải kết nối lại.

---

## Trong gói có gì

| Loại | Slug | Việc |
|---|---|---|
| Plugin | `javis-gate` | Cửa OAuth, khoá riêng và địa chỉ MCP cho ChatGPT, Claude và công cụ AI khác, cùng một trang cài đặt riêng |

AI bên ngoài dùng đúng bộ công cụ SenOS đã có (kết nối MCP, brain, nhắc lịch, Kanban, plugin), cộng năm công cụ chỉ có ở cổng này:

| Công cụ | Việc | Mức quyền |
|---|---|---|
| `javis_chat_find` | Tìm hội thoại theo tên hoặc nội dung | Mọi mức |
| `javis_chat_read` | Đọc các tin cuối của một hội thoại | Mọi mức |
| `javis_chat_send` | Nhắn vào hội thoại để SenOS làm, rồi chờ câu trả lời. Kèm được model và effort | Chỉ Toàn quyền |
| `javis_chat_result` | Chờ tiếp câu trả lời khi SenOS làm lâu | Mọi mức |
| `javis_chat_updates` | Đọc mọi kết quả SenOS đã xong mà AI đó chưa đọc, ở mọi hội thoại | Mọi mức |
| `javis_chat_models` | Xem SenOS có những model nào, thang effort, và hội thoại đang chạy model nào | Mọi mức |
| `javis_chat_note` | Ghi lại cuộc chat bên ChatGPT/Claude vào SenOS: bạn hỏi gì, đã chốt gì | Ghi nháp, Toàn quyền |

## Cần có gì

- **SenOS 0.440.0 trở lên.** Bản cũ hơn thì gói bị tắt kèm lý do ngay lúc cài.
- **Gói trả phí** của ChatGPT (Plus, Pro, Business, Enterprise, Edu) hoặc của Claude (Pro, Max, Team, Enterprise).
- **Máy tính** cho bước cài đặt lần đầu.
- **SenOS có địa chỉ https.** ChatGPT và Claude không nhận địa chỉ kiểu `http://12.34.56.78:7777`. Gắn tên miền riêng trước (Cài đặt, mục Giọng nói, thương hiệu và truy cập).
- **SenOS đã đặt mật khẩu quản trị.** Bước cho phép dựa vào đăng nhập dashboard. Chưa có mật khẩu thì cổng này đóng.

---

## Bước 1: Cài gói và lấy địa chỉ

1. Mở **Chợ Sen**, tìm **SenOS Gate**, bấm cài và đồng ý chạy mã.
2. Vào trang **Plugin**, tìm thẻ **SenOS Gate**, bấm **Mở trang**.
3. Bấm **Chép địa chỉ**. Nó có dạng `https://ten-mien-cua-ban/ext/javis-gate/mcp`.

Trang của gói đầu tiên cho biết cổng đã **Sẵn sàng kết nối** chưa. Mọi hướng dẫn trên trang nằm sau **nút i** cạnh từng mục: bấm mới mở, có các bước cho ChatGPT, Claude và công cụ khác.

## Bước 2a: Nối với ChatGPT

1. Gói **Business**: quản trị viên vào **Workspace settings, Permissions & roles, Connected data**, bật **Create custom MCP connectors**.
2. Trên chatgpt.com (máy tính): **Settings, Apps & Connectors, Advanced settings**, bật **Developer mode**.
3. Vẫn ở **Apps & Connectors**, bấm **Create**, điền:

| Ô | Điền gì |
|---|---|
| Name | `SenOS` |
| MCP Server URL | địa chỉ đã chép ở bước 1 |
| Authentication | **OAuth** |

4. Tích ô xác nhận tin tưởng connector, bấm **Create**.

## Bước 2b: Nối với Claude

1. Trên claude.ai (hoặc app Claude Desktop): **Settings, Connectors**, bấm **Add custom connector**.
2. Đặt tên `SenOS`, dán địa chỉ đã chép ở bước 1, bấm **Add**.
3. Bấm **Connect** trên connector vừa tạo.

Gói Team hay Enterprise thì chủ sở hữu tổ chức thêm connector trước ở phần quản trị, thành viên chỉ cần bấm Connect.

> Tên các mục có thể hơi khác theo phiên bản ChatGPT hay Claude. Tìm chữ "Connectors" trong phần Settings.

## Bước 2c: Nối công cụ AI khác

Mọi công cụ có chỗ thêm "MCP server" bằng địa chỉ đều nối được. Tuỳ công cụ đăng nhập kiểu nào:

**Công cụ chạy trên chính máy bạn và đăng nhập OAuth** (Claude Code, Claude Desktop, Codex CLI, Gemini CLI...): dán địa chỉ ở bước 1, làm theo trang Cho phép như ChatGPT. SenOS tự nhận vì mã đăng nhập chỉ quay về chính máy bạn.

**Công cụ web khác đăng nhập OAuth** (Le Chat, Copilot...): lần đầu SenOS từ chối, để kẻ gian không tự nối được. Rồi:

1. Mở trang của gói (trang Plugin, thẻ SenOS Gate, **Mở trang**), mục **Công cụ AI khác**, phần **Đang xin kết nối**.
2. Thấy địa chỉ của công cụ bạn vừa nối (ví dụ `https://chat.mistral.ai`), bấm **Cho phép**. Ứng dụng trên máy có địa chỉ kiểu `cursor://...` cũng làm vậy.
3. Kết nối lại từ công cụ đó, làm theo trang Cho phép như ChatGPT.

Chỉ cho phép địa chỉ của công cụ **bạn vừa tự nối**. Thấy một địa chỉ lạ thì cứ để đó, nó tự mất sau 7 ngày. Bấm **Bỏ** là địa chỉ đó không xin quyền mới được nữa.

**Công cụ chỉ cho dán khoá vào header** (n8n, script của bạn, trình soạn mã không đăng nhập OAuth được):

1. Trên trang của gói, mục **Công cụ AI khác**, phần **Khoá riêng**, gõ tên công cụ (ví dụ `n8n`) rồi bấm **Tạo khoá**.
2. **Chép ngay**: SenOS chỉ hiện khoá này một lần. Trang có sẵn đoạn cấu hình mẫu.
3. Trong công cụ: địa chỉ là địa chỉ ở bước 1, header `Authorization: Bearer <khoá>`.

Tên khoá là tên hiện trên khung chat của SenOS ("từ n8n"). Ai cầm khoá là dùng được SenOS ở mức quyền bạn chọn, nên đừng dán vào chỗ công khai. Không dùng nữa thì bấm **Thu hồi**, công cụ đó mất kết nối ngay.

## Bước 3: Cho phép

ChatGPT hoặc Claude mở một trang của SenOS.

- Trình duyệt chưa đăng nhập SenOS thì trang hiện ô đăng nhập ngay tại chỗ (có cả ô mã 2 lớp nếu bạn đã bật).
- Trang tiếp theo nói rõ AI đó được làm gì và đang ở mức quyền nào. Bấm **Cho phép**.

## Bước 4: Dùng

Bật connector SenOS trong khung chat (ChatGPT: dấu **+**, chọn **Developer mode**, bật **SenOS**; Claude: nút công cụ, bật **SenOS**). Thử:

- "Trên SenOS có những hội thoại nào gần đây?"
- "Đọc hội thoại Viết Web trên SenOS rồi tư vấn anh nên làm gì tiếp."
- "Ok, bảo SenOS làm theo phương án 2."
- "Ghi lại vào SenOS những gì mình vừa chốt."

### SenOS nắm luôn ngữ cảnh bên ChatGPT, Claude (cần SenOS 0.441.0)

SenOS không đọc được lịch sử chat trên chatgpt.com hay claude.ai, nên AI bên đó **tự ghi lại** phần đáng giữ: bạn hỏi gì, đã chốt gì, vì sao. Nó ghi khi bạn vừa quyết một việc, không ghi sau mọi câu.

- Mỗi cuộc chat bên đó có một hội thoại riêng trong Lịch sử của SenOS, ví dụ **Từ ChatGPT: Kế hoạch Tết**.
- Ghi chép **không tốn hạn mức** bộ não của SenOS, nhưng vẫn vào trí nhớ và vòng tự học. Lần sau hỏi SenOS, nó nhớ bạn đã quyết gì.
- Muốn ghi vào đúng một hội thoại có sẵn của SenOS (ví dụ "Viết Web"), bảo AI đó: "ghi vào hội thoại Viết Web trên SenOS".
- Cần đủ lịch sử nguyên văn thì xuất dữ liệu từ ChatGPT (Settings, Data controls, Export) hay Claude (Settings, Privacy, Export data), rồi đưa tệp cho SenOS đọc.

### Claude Code và Codex: tự lưu mọi lượt chat vào SenOS (SenOS Sync)

AI viết code (Claude Code, Codex) bận làm việc nên gần như không tự ghi chép. Với chúng, SenOS có **SenOS Sync**: mỗi lượt
xong, câu bạn gõ và câu trả lời cuối của AI tự vào Lịch sử của SenOS, tên **Từ Claude Code: <dự án>: <câu đầu>** hay **Từ
Codex: ...**.

1. Nối Claude Code hay Codex vào Gate như mục Bước 2b, 2c.
2. Nó hỏi bạn một câu: "Bật SenOS Sync không?". Trả lời **ok**.
3. Nó tự cài trên máy, báo lại. Khởi động lại Claude Code hay Codex là chạy.

- Không hỏi thì nhắn nó **"bật SenOS Sync"**.
- Không tốn hạn mức của SenOS. API key lọt vào câu chữ được che trước khi lưu. SenOS tắt thì lượt chờ, gửi bù sau.
- Token nó dùng **chỉ lưu được hội thoại**, không làm được gì khác. Xem và thu hồi ở trang **Tích hợp**, tab **Token API**.
- Cần mức **Ghi nháp** hoặc **Toàn quyền**, Python 3.8 trở lên trên máy đó, và bản SenOS có công cụ `javis_sync_setup`.

### Đổi model và effort ngay trong câu lệnh

Cần bản SenOS có công cụ `javis_chat_models`. Cách thử nhanh: hỏi ChatGPT "SenOS có những model nào?". Nó liệt kê được là máy bạn đã có.

Nói với ChatGPT (hay Claude) như nói với người:

- "Bảo SenOS viết lại trang chủ, dùng Opus, effort cao."
- "Việc này nhẹ, cho SenOS chạy Sonnet effort thấp thôi."
- "Hội thoại Viết Web quay về model mặc định nhé."

Hai thứ này chạy khác nhau, có chủ ý:

| | Đổi tới đâu | Vì sao |
|---|---|---|
| **Model** | Ghim cho **đúng hội thoại đó**, y như bạn chọn trên thanh model của khung chat. Chip trên SenOS hiện đúng model mới, các tin sau của hội thoại (kể cả tin bạn tự gõ) chạy model đó cho tới khi đổi lại. | Bạn nhìn thấy và đổi lại được bất cứ lúc nào. Hội thoại khác không bị kéo theo. |
| **Effort** | **Chỉ cho đúng tin đó.** Tin sau quay về mức của hội thoại. Không đổi gì trong cài đặt. | Effort trên khung chat là của cả thẻ model: ChatGPT mà đổi nó là đổi luôn mọi hội thoại khác và việc chạy nền. |

- Thang effort của SenOS: `off`, `low`, `medium`, `high`, `xhigh`, `ultra` (mức cao nhất engine có). ChatGPT nói "max" hay "cao" thì SenOS tự hiểu.
- Tên model trùng ở hai thẻ (ví dụ Opus ở cả gói Claude Code lẫn Anthropic API) thì SenOS **không đoán**, trả lại cho ChatGPT hai lựa chọn kèm tên thẻ để nó hỏi bạn. Đoán nhầm là chuyển sang thẻ tính tiền theo API.
- Đang lúc SenOS trả lời trong hội thoại đó thì không đổi được model hay effort (lượt đang chạy đã chọn xong). ChatGPT chờ lượt xong rồi gửi lại.

### SenOS làm lâu: ChatGPT chờ lâu hơn, và chuông báo khi xong

ChatGPT và Claude **không cho máy ngoài đánh thức một cuộc chat** (tới 11/2026 chưa có đường chính thức nào cho chat thường), nên SenOS không thể tự "gõ cửa" ChatGPT. Gói làm ba việc thay vào đó:

1. **ChatGPT chờ lâu hơn trong cùng một lượt trả lời**, tới khoảng 10 phút, thay vì bỏ cuộc sau nửa phút. Việc vừa phải thì bạn cứ ngồi đó, nó tự đọc kết quả và tư vấn tiếp.
2. **Quá lâu, ChatGPT thôi chờ thì SenOS báo bạn khi xong.** Lượt chat xong mà sau 1 phút ChatGPT vẫn chưa đọc, SenOS để câu trả lời vào **chuông** (đẩy về điện thoại nếu bạn đã bật thông báo), kèm câu cần nhắn sang ChatGPT. Việc nào ChatGPT đã tự đọc thì không báo, để khỏi ồn.
3. **Một câu là đủ:** mở ChatGPT, nhắn **"xem kết quả SenOS"** (hoặc "SenOS xong chưa", "xem tiếp"). Nó lấy mọi kết quả chưa đọc, ở mọi hội thoại, **kể cả khi bạn mở một cuộc chat mới** bên ChatGPT, rồi tư vấn bước tiếp theo.

---

## Mức quyền

Chọn trên trang của gói (trang Plugin, nút **Mở trang**). Đổi xong có hiệu lực ngay, không cần kết nối lại.

| Mức | AI bên ngoài được làm gì |
|---|---|
| **Toàn quyền** (mặc định) | Đọc dữ liệu, nhắn vào khung chat để SenOS làm, và làm việc thật: gửi tin, tạo đơn, đăng bài |
| **Tự làm có giới hạn** | Đọc dữ liệu, đọc hội thoại, ghi chép và viết nháp. Không nhắn vào khung chat, không làm việc ra bên ngoài |
| **Chỉ đọc và gợi ý** | Chỉ đọc, kể cả đọc hội thoại. Không ghi file, không ghi chép, không nhắn vào khung chat |

SenOS tự chặn ở phía mình theo mức đã chọn. AI bên ngoài không tự nâng quyền được.

## Ngắt kết nối

- **Tạm dừng:** tắt gói **SenOS Gate** ở Chợ Sen. Kết nối cũ giữ nguyên, bật lại là dùng tiếp.
- **Ngắt hẳn:** bấm **Ngắt mọi kết nối** trên trang của gói, kể cả mọi khoá riêng. Muốn dùng lại thì nối lại từ bước 2.
- **Ngắt một AI:** mục **Đang kết nối** trên trang của gói liệt kê từng AI theo tên. Bấm **Ngắt** cạnh AI đó (khoá riêng thì bấm **Thu hồi**). Các AI khác vẫn chạy.
- **Gỡ gói:** gỡ ở Chợ Sen. Mọi đường của gói biến mất cùng lúc.

---

## Điều cần biết trước

- **AI bên ngoài không tự thức dậy.** Nó chỉ đọc được câu trả lời của SenOS trong lúc nó đang trả lời bạn. Việc dài thì kết quả luôn nằm trên khung chat của SenOS, chuông SenOS báo khi xong, và bạn nhắn AI kia "xem kết quả SenOS".
- **Tin nhắn vào khung chat tốn hạn mức bộ não của SenOS.** Lượt đó chạy bằng model bạn chọn cho SenOS (Claude Code, Codex...), như khi bạn tự gõ. Phần tư vấn bên ChatGPT hay Claude thì tốn hạn mức gói bên đó.
- **Chỉ nhắn được vào hội thoại của bạn** (khung Trò chuyện, chat với Cộng sự). Hội thoại của khách và nhóm chat thì AI bên ngoài không đọc, không nhắn được.
- **Công cụ ngoài khung chat làm việc trên brain đang mở gần nhất.** Kết quả mỗi công cụ có ghi rõ đang ở brain nào. Tin nhắn vào khung chat thì chạy trên brain của chính hội thoại đó.

## Khi không chạy

| Bạn thấy | Nguyên nhân | Làm gì |
|---|---|---|
| Không có mục Developer mode (ChatGPT) | Gói miễn phí, hoặc đang ở app điện thoại | Dùng gói trả phí, mở chatgpt.com trên máy tính |
| Không có nút Add custom connector (Claude) | Gói miễn phí, hoặc tổ chức chưa cho phép | Dùng gói trả phí, hỏi chủ sở hữu tổ chức |
| Công cụ AI khác báo không kết nối được | Địa chỉ quay về của nó chưa được cho phép | Trang của gói, mục Công cụ AI khác, bấm Cho phép, rồi kết nối lại (Bước 2c) |
| Công cụ dùng khoá riêng báo 401 | Khoá đã bị thu hồi, hoặc đã bấm Ngắt mọi kết nối | Tạo khoá mới |
| Báo không kết nối được server | Địa chỉ không phải https, gói đang tắt, hoặc SenOS chưa có mật khẩu | Xem lại "Cần có gì" và bước 1 |
| AI báo cần mức Toàn quyền khi nhắn vào khung chat | Gói đang ở mức thấp hơn | Nâng mức quyền trên trang của gói |
| AI không đổi được model, hoặc không có `javis_chat_models` | SenOS chưa lên bản có tính năng này | Cập nhật SenOS |
| AI báo "several connected models match" | Tên model có ở hai thẻ | Nói rõ thẻ nào (gói Claude Code hay API), AI gửi lại |
| Việc xong mà chuông không kêu | ChatGPT đã tự đọc kết quả, hoặc điện thoại chưa bật thông báo SenOS | Bình thường nếu ChatGPT đã đọc. Bật thông báo trong Cài đặt của SenOS |
| Trang SenOS báo "Yêu cầu này đã quá hạn" | Để trang Cho phép mở quá 10 phút | Kết nối lại từ ChatGPT hoặc Claude |
| Đang dùng tốt bỗng bắt kết nối lại | 30 ngày không dùng, hoặc đã bấm Ngắt mọi kết nối | Kết nối lại |

## An toàn

- Token chỉ lưu dạng băm trong thư mục dữ liệu riêng của gói, không nằm trong brain.
- Cổng chỉ trả mã về đúng máy của OpenAI (`chatgpt.com`, `*.openai.com`), của Anthropic (`claude.ai`, `claude.com`), chính máy của bạn (`localhost`, cho Claude Code và Claude Desktop), hoặc địa chỉ **chính bạn** bấm Cho phép trên trang của gói (trang đòi đăng nhập SenOS). Không bao giờ nhận địa chỉ `http` của máy khác. Kẻ gian tự đăng ký một kết nối trỏ về máy mình sẽ không nhận được mã.
- Khoá riêng chỉ bạn tạo được, chỉ hiện một lần, và cũng chỉ lưu dạng băm.
- Token của gói này tách hẳn khỏi token Claude Code và Codex dùng. Ngắt bên này không ảnh hưởng bên kia.
- Refresh token xoay vòng: một token cũ bị dùng lại là SenOS thu hồi cả chuỗi và bắt cho phép lại.
