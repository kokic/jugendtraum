#pragma once

#include "../AgableMob.h"

class WaterAnimal : public AgableMob
{
public:
	WaterAnimal(BlockSource &);
	virtual ~WaterAnimal();
	virtual void normalTick();
	virtual void readAdditionalSaveData(const CompoundTag *);
	virtual void addAdditionalSaveData(CompoundTag *);
	virtual bool isWaterMob();
	virtual void getAmbientSoundInterval();
	virtual float getBaseSpeed();
	virtual bool canSpawn();
	virtual void removeWhenFarAway();
	void getExperienceReward(Player *);
};
