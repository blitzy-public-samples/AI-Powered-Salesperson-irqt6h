import unittest
from unittest.mock import patch, MagicMock
from services.nlp_processor import NLPProcessor
from services.rag_engine import RAGEngine
from services.quote_generator import QuoteGenerator
from services.sku_catalog import SKUCatalog

class TestNLPProcessor(unittest.TestCase):
    def setUp(self):
        self.nlp_processor = NLPProcessor()

    def test_process_text(self):
        text = "This is a sample text for NLP processing."
        result = self.nlp_processor.process_text(text)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
        self.assertIn('entities', result)
        self.assertIn('sentiment', result)

    def test_extract_keywords(self):
        text = "Artificial intelligence and machine learning are transforming industries."
        keywords = self.nlp_processor.extract_keywords(text)
        self.assertIsInstance(keywords, list)
        self.assertIn('artificial intelligence', keywords)
        self.assertIn('machine learning', keywords)

class TestRAGEngine(unittest.TestCase):
    @patch('services.rag_engine.VectorStore')
    def setUp(self, mock_vector_store):
        self.mock_vector_store = mock_vector_store
        self.rag_engine = RAGEngine(self.mock_vector_store)

    def test_retrieve_relevant_documents(self):
        query = "What are the benefits of solar energy?"
        mock_docs = [MagicMock() for _ in range(3)]
        self.mock_vector_store.similarity_search.return_value = mock_docs
        
        results = self.rag_engine.retrieve_relevant_documents(query)
        
        self.assertEqual(len(results), 3)
        self.mock_vector_store.similarity_search.assert_called_once_with(query, k=3)

    def test_generate_answer(self):
        query = "Explain quantum computing"
        context = "Quantum computing uses quantum bits or qubits..."
        
        with patch('services.rag_engine.LLMChain') as mock_llm_chain:
            mock_llm_chain.return_value.run.return_value = "Quantum computing is a type of computation that harnesses quantum mechanical phenomena..."
            
            answer = self.rag_engine.generate_answer(query, context)
            
            self.assertIsInstance(answer, str)
            self.assertTrue(len(answer) > 0)
            mock_llm_chain.return_value.run.assert_called_once()

class TestQuoteGenerator(unittest.TestCase):
    def setUp(self):
        self.quote_generator = QuoteGenerator()

    def test_generate_quote(self):
        products = [
            {"sku": "PROD001", "quantity": 2, "unit_price": 10.99},
            {"sku": "PROD002", "quantity": 1, "unit_price": 24.99}
        ]
        customer_info = {
            "name": "John Doe",
            "email": "john@example.com",
            "address": "123 Main St, Anytown, USA"
        }
        
        quote = self.quote_generator.generate_quote(products, customer_info)
        
        self.assertIsInstance(quote, dict)
        self.assertIn('quote_id', quote)
        self.assertIn('total_price', quote)
        self.assertIn('products', quote)
        self.assertIn('customer_info', quote)
        self.assertEqual(len(quote['products']), 2)
        self.assertEqual(quote['customer_info'], customer_info)

    def test_calculate_total_price(self):
        products = [
            {"sku": "PROD001", "quantity": 2, "unit_price": 10.99},
            {"sku": "PROD002", "quantity": 1, "unit_price": 24.99}
        ]
        
        total_price = self.quote_generator.calculate_total_price(products)
        
        expected_total = (2 * 10.99) + 24.99
        self.assertAlmostEqual(total_price, expected_total, places=2)

class TestSKUCatalog(unittest.TestCase):
    def setUp(self):
        self.sku_catalog = SKUCatalog()

    @patch('services.sku_catalog.requests.get')
    def test_fetch_sku_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "sku": "PROD001",
            "name": "Sample Product",
            "description": "This is a sample product",
            "price": 19.99
        }
        mock_get.return_value = mock_response

        sku = "PROD001"
        details = self.sku_catalog.fetch_sku_details(sku)

        self.assertIsInstance(details, dict)
        self.assertEqual(details['sku'], sku)
        self.assertIn('name', details)
        self.assertIn('description', details)
        self.assertIn('price', details)
        mock_get.assert_called_once_with(f"{self.sku_catalog.api_base_url}/sku/{sku}")

    def test_search_skus(self):
        query = "solar panel"
        mock_results = [
            {"sku": "SOLAR001", "name": "100W Solar Panel"},
            {"sku": "SOLAR002", "name": "200W Solar Panel"}
        ]

        with patch.object(self.sku_catalog, '_search_api', return_value=mock_results):
            results = self.sku_catalog.search_skus(query)

            self.assertIsInstance(results, list)
            self.assertEqual(len(results), 2)
            self.assertEqual(results[0]['sku'], "SOLAR001")
            self.assertEqual(results[1]['sku'], "SOLAR002")

if __name__ == '__main__':
    unittest.main()