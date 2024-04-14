# Utilitary imports
import importlib
import pytest
from unittest.mock import patch, MagicMock

# Local imports
import src.config.mongodb as mongodb_module


class TestConfig:
    @pytest.fixture
    def mock_env_vars(self):
        return {
            'MONGO_DB_USERNAME': 'test_username',
            'MONGO_DB_PWD': 'test_password',
            'MONGO_DB_NAME': 'test_db',
        }

    @patch('src.config.mongodb.os.environ.get')
    @patch('src.config.mongodb.load_dotenv')
    @patch('src.config.mongodb.PyMongo')
    def test_mongodb_config(self,
                            mock_pymongo, 
                            mock_load_dotenv, 
                            mock_get_env, 
                            mock_env_vars):
        # ARRANGE
        mock_get_env.side_effect = lambda key: mock_env_vars[key]
        mock_load_dotenv.return_value = None
        mock_pymongo.return_value = MagicMock()

        expected_db_config = {
            'username': 'test_username',
            'password': 'test_password',
            'db': 'test_db',
        }

        # ACT
        importlib.reload(mongodb_module)

        # ASSERT
        assert mongodb_module.db_config == expected_db_config
