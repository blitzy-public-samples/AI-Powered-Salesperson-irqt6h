import pytest
from unittest.mock import AsyncMock, patch
from backend.tasks import process_chat_message, generate_quote

@pytest.mark.asyncio
async def test_process_chat_message():
    mock_message = {
        "user_id": "test_user",
        "content": "Hello, world!",
        "timestamp": "2023-06-01T12:00:00Z"
    }
    
    with patch('backend.tasks.save_message_to_db') as mock_save:
        mock_save.return_value = AsyncMock()
        await process_chat_message(mock_message)
        mock_save.assert_called_once_with(mock_message)

@pytest.mark.asyncio
async def test_generate_quote():
    mock_user = {
        "id": "test_user",
        "name": "John Doe",
        "preferences": ["inspirational", "motivational"]
    }
    
    with patch('backend.tasks.fetch_quote_from_api') as mock_fetch:
        mock_fetch.return_value = AsyncMock(return_value={
            "quote": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs"
        })
        
        result = await generate_quote(mock_user)
        
        assert "quote" in result
        assert "author" in result
        mock_fetch.assert_called_once_with(mock_user["preferences"])

# HUMAN ASSISTANCE NEEDED
# The following test cases might need to be expanded based on the actual implementation details:
# - Test error handling in process_chat_message
# - Test rate limiting in generate_quote
# - Test different user preferences scenarios in generate_quote
# - Test caching mechanism if implemented