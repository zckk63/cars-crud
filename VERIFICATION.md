# Cars CRUD 课堂作业验证记录

验证日期：2026-10-12。项目位于原文件夹 Desktop/pf/cars-crud。

## 2.2 Testing Workshop

新增四个文件，每个包含一个讲义示例和一个自主测试，共 8 个测试：

| 层级 | 文件 | 自主测试 |
| --- | --- | --- |
| 单元 | tests/unit/test_workshop_unit.py | 空白 model 被拒绝 |
| 集成 | tests/integration/test_workshop_integration.py | 删除一辆车不影响另一辆 |
| API | tests/api/test_workshop_api.py | 非法年份返回 422 且不写入数据库 |
| 浏览器 E2E | tests/e2e/test_workshop_e2e.py | 编辑车辆后刷新，修改仍然存在 |

四组均实际完成“示例通过 → 故意修改断言并失败 → 恢复后两个测试通过”。最终文件中没有保留故意错误。

- 作业新增测试：8 passed。
- 整个项目：66 passed，1 个依赖弃用警告，无失败。
- 浏览器测试运行真实 Chromium、HTTP 服务及隔离 SQLite 数据库；覆盖创建、查看、编辑、刷新持久化、删除、取消操作和校验。
- 为使从项目根目录运行全部测试正常，将 --headed 注册从 tests/e2e/conftest.py 移到 tests/conftest.py。
- 日志保存在 assignment-results/，其中 02-intentional-failure 文件中的失败是课堂练习的预期结果。

## 环境与重新运行

本次自动验证使用项目 .venv 中的 Python 3.12.14，符合讲义 Python >= 3.11 要求。电脑上另行安装的 Python 3.11.9 未卸载。当前 .venv 不是 3.11 环境。

在项目文件夹打开 PowerShell，执行：

```powershell
$env:PLAYWRIGHT_BROWSERS_PATH = "$PWD\.venv\playwright-browsers"
.\.venv\Scripts\python.exe -m pytest -v
```

只运行作业测试：

```powershell
.\.venv\Scripts\python.exe -m pytest tests/unit/test_workshop_unit.py tests/integration/test_workshop_integration.py tests/api/test_workshop_api.py tests/e2e/test_workshop_e2e.py -v
```

启动网页：

```powershell
.\.venv\Scripts\python.exe -m uvicorn app.main:app --reload
```

浏览器访问 http://127.0.0.1:8000 ，结束服务按 Ctrl+C。

## 测试层级解释

单元测试只调用数据校验模型；集成测试使用真正 SQLite 文件验证数据库函数；API 测试通过 TestClient 检查 HTTP 状态、JSON 和数据库效果；E2E 测试通过浏览器操作网页，经过 JavaScript、HTTP、后端和数据库，验证完整用户流程。
