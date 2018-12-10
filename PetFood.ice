module PetFoodSensors{
        interface SensorControl{
                void motorTime(string time);
                void givefood(int weight);
                int getContainerFood();
                int getFoodEated();
                bool eatingNow();
		int getWeight();                
        };
};
