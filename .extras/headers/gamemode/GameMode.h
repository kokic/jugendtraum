#pragma once

#include <functional>

class PacketSender;
class Level;
class SoundPlayer;
class Vibration;
class Entity;
class Player;
class BlockPos;
class Vec3;
class ItemInstance;
class InputMode;

class GameMode {
public:
	GameMode(PacketSender&, Level&, SoundPlayer&, Vibration&);

	virtual ~GameMode();
	virtual void startDestroyBlock(Player&, BlockPos, signed char);
	virtual void destroyBlock(Player&, BlockPos, signed char);
	virtual void continueDestroyBlock(Player&, BlockPos, signed char);
	virtual void stopDestroyBlock(Player&);
	virtual void startBuildBlock(Player&, BlockPos, signed char);
	virtual void buildBlock(Player&, BlockPos, signed char);
	virtual void continueBuildBlock(Player&, BlockPos, signed char);
	virtual void stopBuildBlock(Player&);
	virtual void tick();
	virtual void getPickRange(Player*, const InputMode&, bool);
	virtual void useItem(ItemInstance&);
	virtual void useItemOn(Player&, ItemInstance*, const BlockPos&, signed char, const Vec3&);
	virtual void interact(Player&, Entity&);
	virtual void attack(Player&, Entity&);
	virtual void releaseUsingItem(Player&);
	virtual void setTrialMode(bool);
	virtual bool isInTrialMode();
};
