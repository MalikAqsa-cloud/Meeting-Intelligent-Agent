import os
import requests
import logging
from typing import List, Dict, Optional

logger = logging.getLogger(__name__)

class TrelloAgent:
    """
    Agent responsible for creating task cards in Trello
    """
    
    def __init__(self):
        self.api_key = os.getenv("TRELLO_API_KEY")
        self.token = os.getenv("TRELLO_TOKEN")
        self.list_id = os.getenv("TRELLO_LIST_ID")
        
        if not all([self.api_key, self.token, self.list_id]):
            logger.warning("Trello credentials not found. Using demo mode.")
            self.demo_mode = True
        else:
            self.demo_mode = False
        
        self.base_url = "https://api.trello.com/1"
    
    async def create_tasks(self, action_items: List[str]) -> List[Dict[str, any]]:
        """
        Create Trello cards for each action item
        
        Args:
            action_items: List of action item strings
            
        Returns:
            List of created card information
        """
        created_cards = []
        
        try:
            logger.info(f"Creating {len(action_items)} Trello cards")
            
            if self.demo_mode:
                # Return demo card creation results
                for i, action_item in enumerate(action_items, 1):
                    created_cards.append({
                        'id': f'demo_card_{i}',
                        'name': action_item,
                        'url': f'https://trello.com/c/demo_card_{i}'
                    })
                logger.info(f"Demo mode: Created {len(created_cards)} demo cards")
                return created_cards
            
            for i, action_item in enumerate(action_items, 1):
                try:
                    # Create card data
                    card_data = {
                        'name': action_item,
                        'desc': f"Action item #{i} from meeting analysis",
                        'idList': self.list_id,
                        'key': self.api_key,
                        'token': self.token
                    }
                    
                    # Make API request to create card
                    response = requests.post(
                        f"{self.base_url}/cards",
                        data=card_data,
                        timeout=10
                    )
                    
                    if response.status_code == 200:
                        card_info = response.json()
                        created_cards.append({
                            'id': card_info['id'],
                            'name': card_info['name'],
                            'url': card_info['url']
                        })
                        logger.info(f"Created Trello card: {action_item}")
                    else:
                        logger.error(f"Failed to create card for '{action_item}': {response.status_code} - {response.text}")
                        
                except Exception as e:
                    logger.error(f"Error creating card for '{action_item}': {str(e)}")
                    continue
            
            logger.info(f"Successfully created {len(created_cards)} out of {len(action_items)} cards")
            return created_cards
            
        except Exception as e:
            logger.error(f"Error in create_tasks: {str(e)}")
            raise
    
    async def test_connection(self) -> bool:
        """
        Test Trello API connection and list access
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            if self.demo_mode:
                logger.info("Demo mode: Trello connection test skipped")
                return True
                
            url = f"{self.base_url}/lists/{self.list_id}"
            params = {
                'key': self.api_key,
                'token': self.token
            }
            
            response = requests.get(url, params=params, timeout=10)
            
            if response.status_code == 200:
                list_info = response.json()
                logger.info(f"Successfully connected to Trello list: {list_info['name']}")
                return True
            else:
                logger.error(f"Trello connection test failed: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            logger.error(f"Trello connection test error: {str(e)}")
            return False
