#pragma once

#include <string>
#include <vector>
#include <memory>
#include <map>
#include <unordered_map>

#include "../client/renderer/texture/TextureUVCoordinateSet.h"
#include "mcpe/util/Color.h"
#include "mcpe/util/BlockID.h"
#include "mcpe/util/Util.h"
#include "mcpe/util/AABB.h"
#include "material/Material.h"
#include "BlockShape.h"
#include "mcpe/item/CreativeItemCategory.h"
#include "BlockSoundType.h"
#include "BlockSupportType.h"
#include "../entity/EntityType.h"
#include "../blockentity/BlockEntityType.h"
#include "BlockState.h"

#define BLOCK_ID_SIZE 256

struct Material;
struct BlockEntity;
struct Container;
struct FullBlock;
struct BlockPos;
struct BlockSource;
struct Entity;
struct Mob;
struct Player;
struct ItemInstance;
struct Random;
struct Vec3;
struct Brightness;
struct Color;

typedef unsigned char uchar;

class Block
{
public:
	uint8_t blockId; // 4
	char filler_Block[400];

	static std::unordered_map<std::string,Block const*> mBlockLookupMap;
	static std::vector<std::unique_ptr<Block>> mOwnedBlocks;
	static Block* mBlocks[BLOCK_ID_SIZE];
	static bool mSolid[BLOCK_ID_SIZE];
	static float mTranslucency[BLOCK_ID_SIZE];
	static uint8_t mLightBlock[BLOCK_ID_SIZE];
	static int mLightEmission[BLOCK_ID_SIZE];
	static bool mPushesOutItems[BLOCK_ID_SIZE];
	static bool mShouldTick[BLOCK_ID_SIZE];

	Block(const std::string&, int, const Material&);

	/* vtable */
	
	virtual ~Block();
	virtual void tick(BlockSource&, BlockPos const&, Random&) const;
	virtual AABB const& getCollisionShape(AABB&, BlockSource&, BlockPos const&, Entity*) const;
	virtual bool isObstructingChests(BlockSource&, BlockPos const&) const;
	virtual Vec3 const& randomlyModifyPosition(BlockPos const&, int&) const;
	virtual Vec3 const& randomlyModifyPosition(BlockPos const&) const;
	virtual void addAABBs(BlockSource&, BlockPos const&, AABB const*, std::vector<AABB, std::allocator<AABB> >&) const;
	virtual AABB const& getAABB(BlockSource&, BlockPos const&, AABB&, int, bool, int) const;
	virtual void addCollisionShapes(BlockSource&, BlockPos const&, AABB const*, std::vector<AABB, std::allocator<AABB> >&, Entity*) const;
	virtual bool canProvideSupport(BlockSource&, BlockPos const&, signed char, BlockSupportType) const;
	virtual bool isInfiniburnBlock(int) const;
	virtual bool isCropBlock() const;
	virtual bool isContainerBlock() const;
	virtual bool isCraftingBlock() const;
	virtual bool isInteractiveBlock() const;
	virtual bool isWaterBlocking() const;
	virtual bool isHurtableBlock() const;
	virtual bool isFenceBlock() const;
	virtual bool isStairBlock() const;
	virtual bool isRailBlock() const;
	virtual bool canHurtAndBreakItem() const;
	virtual bool isSignalSource() const;
	virtual bool isValidAuxValue(int) const;
	virtual int getDirectSignal(BlockSource&, BlockPos const&, int) const;
	virtual bool waterSpreadCausesSpawn() const;
	virtual bool shouldConnectToRedstone(BlockSource&, BlockPos const&, int) const;
	virtual void handleRain(BlockSource&, BlockPos const&, float) const;
	virtual float getThickness() const;
	virtual bool checkIsPathable(Entity&, BlockPos const&, BlockPos const&) const;
	virtual void dispense(BlockSource&, Container&, int, Vec3 const&, signed char) const;
	virtual void onPlace(BlockSource&, BlockPos const&) const;
	virtual void onRemove(BlockSource&, BlockPos const&) const;
	virtual void onExploded(BlockSource&, BlockPos const&, Entity*) const;
	virtual void onStepOn(Entity&, BlockPos const&) const;
	virtual void onFallOn(BlockSource&, BlockPos const&, Entity*, float) const;
	virtual void transformOnFall(BlockSource&, BlockPos const&, Entity*, float) const;
	virtual void onRedstoneUpdate(BlockSource&, BlockPos const&, int, bool) const;
	virtual void onMove(BlockSource&, BlockPos const&, BlockPos const&) const;
	virtual bool detachesOnPistonMove(BlockSource&, BlockPos const&) const;
	virtual void onLoaded(BlockSource&, BlockPos const&) const;
	virtual int getRedstoneProperty(BlockSource&, BlockPos const&) const;
	virtual void updateEntityAfterFallOn(Entity&) const;
	virtual void onFertilized(BlockSource&, BlockPos const&, Entity*) const;
	virtual bool mayConsumeFertilizer(BlockSource&) const;
	virtual bool mayPick() const;
	virtual bool mayPick(BlockSource&, int, bool) const;
	virtual bool mayPlace(BlockSource&, BlockPos const&, signed char) const;
	virtual bool mayPlace(BlockSource&, BlockPos const&) const;
	virtual bool mayPlaceOn(Block const&) const;
	virtual void tryToPlace(BlockSource&, BlockPos const&, unsigned char) const;
	virtual void breaksFallingBlocks(int) const;
	virtual void destroy(BlockSource&, BlockPos const&, int, Entity*) const;
	virtual void playerWillDestroy(Player&, BlockPos const&, int) const;
	virtual void getIgnoresDestroyPermissions(Entity&, BlockPos const&) const;
	virtual void neighborChanged(BlockSource&, BlockPos const&, BlockPos const&) const;
	virtual AABB const& getSecondPart(BlockSource&, BlockPos const&, BlockPos&) const;
	virtual int getResource(Random&, int, int) const;
	virtual int getResourceCount(Random&, int, int) const;
	virtual void asItemInstance(BlockSource&, BlockPos const&, int) const;
	virtual void spawnResources(BlockSource&, BlockPos const&, int, float, int) const;
	virtual void spawnBurnResources(BlockSource&, float, float, float);
	virtual float getExplosionResistance(Entity*) const;
	virtual void clip(BlockSource&, BlockPos const&, Vec3 const&, Vec3 const&, bool, int) const;
	virtual bool use(Player&, BlockPos const&) const;
	virtual int getPlacementDataValue(Entity&, BlockPos const&, signed char, Vec3 const&, int) const;
	virtual void calcVariant(BlockSource&, BlockPos const&, unsigned char) const;
	virtual bool isAttachedTo(BlockSource&, BlockPos const&, BlockPos&) const;
	virtual void attack(Player*, BlockPos const&) const;
	virtual void handleEntityInside(BlockSource&, BlockPos const&, Entity*, Vec3&) const;
	virtual bool entityInside(BlockSource&, BlockPos const&, Entity&) const;
	virtual void playerDestroy(Player*, BlockPos const&, int) const;
	virtual bool canSurvive(BlockSource&, BlockPos const&) const;
	virtual int getExperienceDrop(Random&) const;
	virtual bool canBeBuiltOver(BlockSource&, BlockPos const&) const;
	virtual void triggerEvent(BlockSource&, BlockPos const&, int, int) const;
	virtual void getMobToSpawn(BlockSource&, BlockPos const&) const;
	virtual Color getMapColor(BlockSource&, BlockPos const&) const;
	virtual Color getMapColor() const;
	virtual bool shouldStopFalling(Entity&) const;
	virtual void calcGroundFriction(Mob&, BlockPos const&) const;
	virtual bool canHaveExtraData() const;
	virtual bool hasComparatorSignal() const;
	virtual int getComparatorSignal(BlockSource&, BlockPos const&, signed char, int) const;
	virtual bool shouldRenderFace(BlockSource&, BlockPos const&, signed char, AABB const&) const;
	virtual int getIconYOffset() const;
	virtual std::string buildDescriptionName(unsigned char) const;
	virtual int getColor(int) const;
	virtual int getColor(BlockSource&, BlockPos const&) const;
	virtual int getColor(BlockSource&, BlockPos const&, unsigned char) const;
	virtual int getColorForParticle(BlockSource&, BlockPos const&, int) const;
	virtual bool isSeasonTinted(BlockSource&, BlockPos const&) const;
	virtual void onGraphicsModeChanged(bool, bool, bool);
	virtual int getRenderLayer(BlockSource&, BlockPos const&) const;
	virtual int getExtraRenderLayers() const;
	virtual const AABB& getVisualShape(BlockSource&, BlockPos const&, AABB&, bool) const;
	virtual const AABB& getVisualShape(unsigned char, AABB&, bool) const;
	virtual int getVariant(int) const;
	virtual signed char getMappedFace(signed char, int) const;
	virtual void animateTick(BlockSource&, BlockPos const&, Random&) const;
	virtual Block* init();
	virtual bool canBeSilkTouched() const;
	virtual ItemInstance getSilkTouchItemInstance(unsigned char) const;
	virtual Block* setVisualShape(AABB const&);
	virtual Block* setVisualShape(Vec3 const&, Vec3 const&);
	virtual Block* setLightBlock(Brightness);
	virtual Block* setLightEmission(float);
	virtual Block* setExplodeable(float);
	virtual Block* setDestroyTime(float);
	virtual Block* setFriction(float);
	virtual Block* setBlockProperty(BlockProperty);
	virtual Block* setTicking(bool);
	virtual Block* setMapColor(Color const&);
	virtual Block* addProperty(BlockProperty);
	virtual void resetBitsUsed();
	virtual int getSpawnResourcesAuxValue(unsigned char) const;
public:
	static Block* lookupByName(std::string const&, bool);
	static void initBlocks();
	static void teardownBlocks();
	static float getLightEmission(BlockID);
	static signed char getPlacementFacingAll(Entity&, BlockPos const&, float);
	static BlockID transformToValidBlockId(BlockID);
	static BlockID transformToValidBlockId(BlockID, BlockPos const&);
	static signed char getPlacementFacingAllExceptAxisY(Entity&, BlockPos const&, float);
public:
	CreativeItemCategory getCreativeCategory() const;
	bool isType(Block const*) const;
	bool hasProperty(BlockProperty) const;
	void getBlockState(BlockState::BlockStates) const;
	float getGravity() const;
	Material const& getMaterial() const;
	int getRenderLayer() const;
	BlockEntityType getBlockEntityType() const;
	bool isSolid() const;
	bool isAlphaTested() const;
	void DEPRECATEDcallOnGraphicsModeChanged(bool, bool, bool);
	float getShadeBrightness() const;
	BlockProperty* getProperties() const;
	float getFriction() const;
	float getDestroySpeed() const;
	std::string getDescriptionId() const;
	bool isSolidBlockingBlock() const;
	void setPushesOutItems(bool);
	void setSolid(bool);
	void setCategory(CreativeItemCategory);
	void setNameId(std::string const&);
	void popResource(BlockSource&, BlockPos const&, ItemInstance const&) const;
	bool canInstatick() const;
	std::string getDebugText(std::vector<std::string, std::allocator<std::string> >&) const;
	bool canGrowChorus() const;
	void getMobToSpawn(BlockSource&, BlockPos const&, std::map<EntityType, int, std::less<EntityType>, std::allocator<std::pair<EntityType const, int> > >, bool&) const;
	bool isUnbreakable() const;
	void getTypeToSpawn(BlockSource&, EntityType, BlockPos const&) const;
	bool hasBlockEntity() const;
	bool pushesOutItems() const;
	void getParticleQuantityScalar() const;
	void clip(BlockSource&, BlockPos const&, Vec3 const&, Vec3 const&, bool, int, AABB const&) const;
	void addAABB(AABB const&, AABB const*, std::vector<AABB, std::allocator<AABB> >&) const;
	bool isHeavy() const;
	bool canSlide() const;
public:
	static Block * mDirt;
	static Block * mChest;
	static Block * mGrass;
	static Block * mTorch;
	static Block * mBookshelf;
	static Block * mSandStone;
	static Block * mWorkBench;
	static Block * mStainedClay;
	static Block * mRedSandstone;
	static Block * mWool;
	static Block * mBrick;
	static Block * mWoodenDoor;
	static Block * mSnow;
	static Block * mSkull;
	static Block * mBed;
	static Block * mLever;
	static Block * mCactus;
	static Block * mBedrock;
	static Block * mPortal;
	static Block * mTallgrass;
	static Block * mWoolCarpet;
	static Block * mDoublePlant;
	static Block * mInvisibleBedrock;
	static Block * mTopSnow;
	static Block * mPiston;
	static Block * mShulkerBox;
	static Block * mSign;
	static Block * mStructureVoid;
	static Block * mAir;
	static Block * mPumpkin;
	static Block * mRedFlower;
	static Block * mWoodPlanks;
	static Block * mWoodButton;
	static Block * mStoneButton;
	static Block * mTNT;
	static Block * mRedMushroom;
	static Block * mNote;
	static Block * mStone;
	static Block * mQuartzBlock;
	static Block * mFenceGateOak;
	static Block * mRedStoneDust;
	static Block * mStickyPiston;
	static Block * mTripwireHook;
	static Block * mYellowFlower;
	static Block * mEndPortalFrame;
	static Block * mCobblestoneWall;
	static Block * mPoweredRepeater;
	static Block * mPoweredComparator;
	static Block * mFire;
	static Block * mAnvil;
	static Block * mCocoa;
	static Block * mTripwire;
	static Block * mInfoUpdateGame1;
	static Block * mTrappedChest;
	static Block * mLeaves;
	static Block * mStoneSlab;
	static Block * mSlimeBlock;
	static Block * mWoodenSlab;
	static Block * mFlowingWater;
	static Block * mGlass;
	static Block * mCobblestone;
	static Block * mStoneBrick;
	static Block * mHardenedClay;
	static Block * mSponge;
	static Block * mEnchantingTable;
	static Block * mEndPortal;
	static Block * mChalkboard;
	static Block * mCameraBlock;
	static Block * mCommandBlock;
	static Block * mChainCommandBlock;
	static Block * mRepeatingCommandBlock;
	static Block * mDeny;
	static Block * mAllow;
	static Block * mBorder;
	static Block * mVine;
	static Block * mFence;
	static Block * mLadder;
	static Block * mCauldron;
	static Block * mWaterlily;
	static Block * mHopper;
	static Block * mFrostedIce;
	static Block * mIronFence;
	static Block * mEndGateway;
	static Block * mEndStone;
	static Block * mObsidian;
	static Block * mBrownMushroom;
	static Block * mClay;
	static Block * mSand;
	static Block * mMelon;
	static Block * mGravel;
	static Block * mMycelium;
	static Block * mPistonArm;
	static Block * mMonsterStoneEgg;
	static Block * mQuartzOre;
	static Block * mDiamondOre;
	static Block * mEmeraldOre;
	static Block * mNetherrack;
	static Block * mRedStoneOre;
	static Block * mGlazedTerracottaRed;
	static Block * mGlazedTerracottaBlue;
	static Block * mGlazedTerracottaCyan;
	static Block * mGlazedTerracottaGray;
	static Block * mGlazedTerracottaLime;
	static Block * mGlazedTerracottaPink;
	static Block * mGlazedTerracottaBlack;
	static Block * mGlazedTerracottaBrown;
	static Block * mGlazedTerracottaGreen;
	static Block * mGlazedTerracottaWhite;
	static Block * mGlazedTerracottaOrange;
	static Block * mGlazedTerracottaPurple;
	static Block * mGlazedTerracottaSilver;
	static Block * mGlazedTerracottaYellow;
	static Block * mGlazedTerracottaMagenta;
	static Block * mGlazedTerracottaLightBlue;
	static Block * mLog;
	static Block * mLog2;
	static Block * mCoalOre;
	static Block * mGoldOre;
	static Block * mIronOre;
	static Block * mLapisOre;
	static Block * mStoneSlab2;
	static Block * mDispenser;
	static Block * mGlowStone;
	static Block * mGoldBlock;
	static Block * mIronBlock;
	static Block * mOakStairs;
	static Block * mGoldenRail;
	static Block * mLitPumpkin;
	static Block * mPrismarine;
	static Block * mSeaLantern;
	static Block * mBirchStairs;
	static Block * mBrickStairs;
	static Block * mNetherBrick;
	static Block * mNetherFence;
	static Block * mPurpurBlock;
	static Block * mStoneStairs;
	static Block * mAcaciaStairs;
	static Block * mDetectorRail;
	static Block * mIronTrapdoor;
	static Block * mJungleStairs;
	static Block * mPurpurStairs;
	static Block * mQuartzStairs;
	static Block * mSpruceStairs;
	static Block * mActivatorRail;
	static Block * mDarkOakStairs;
	static Block * mBirchFenceGate;
	static Block * mSpuceFenceGate;
	static Block * mAcaciaFenceGate;
	static Block * mJungleFenceGate;
	static Block * mSandstoneStairs;
	static Block * mDarkOakFenceGate;
	static Block * mDaylightDetector;
	static Block * mLitRedStoneTorch;
	static Block * mMossyCobblestone;
	static Block * mStoneBrickStairs;
	static Block * mNetherBrickStairs;
	static Block * mUnlitRedStoneLamp;
	static Block * mWoodPressurePlate;
	static Block * mRedSandstoneStairs;
	static Block * mStonePressurePlate;
	static Block * mHeavyWeightedPressurePlate;
	static Block * mLightWeightedPressurePlate;
	static Block * mRail;
	static Block * mEndRod;
	static Block * mDropper;
	static Block * mEndBrick;
	static Block * mObserver;
	static Block * mTrapdoor;
	static Block * mGlassPane;
	static Block * mEnderChest;
	static Block * mConcretePowder;
	static Block * mBeacon;
	static Block * mFurnace;
	static Block * mCoalBlock;
	static Block * mDragonEgg;
	static Block * mFlowerPot;
	static Block * mItemFrame;
	static Block * mPackedIce;
	static Block * mLapisBlock;
	static Block * mMobSpawner;
	static Block * mFlowingLava;
	static Block * mBrewingStand;
	static Block * mDiamondBlock;
	static Block * mEmeraldBlock;
	static Block * mStainedGlass;
	static Block * mRedstoneBlock;
	static Block * mDoubleStoneSlab;
	static Block * mChorusPlantBlock;
	static Block * mDoubleStoneSlab2;
	static Block * mRedMushroomBlock;
	static Block * mStainedGlassPane;
	static Block * mStonecutterBench;
	static Block * mChorusFlowerBlock;
	static Block * mUnpoweredRepeater;
	static Block * mBrownMushroomBlock;
	static Block * mUnpoweredComparator;
	static Block * mIce;
	static Block * mWeb;
	static Block * mCake;
	static Block * mReeds;
	static Block * mPodzol;
	static Block * mLeaves2;
	static Block * mSapling;
	static Block * mConcrete;
	static Block * mDeadBush;
	static Block * mHayBlock;
	static Block * mSoulSand;
	static Block * mWallSign;
	static Block * mLitRedStoneOre;
	static Block * mGlowingObsidian;
	static Block * mGrassPathBlock;
	static Block * mFarmland;
	static Block * mStillWater;
	static Block * mMelonStem;
	static Block * mStillLava;
	static Block * mWheatCrop;
	static Block * mCarrotCrop;
	static Block * mLitFurnace;
	static Block * mNetherWart;
	static Block * mPotatoCrop;
	static Block * mMovingBlock;
	static Block * mPumpkinStem;
	static Block * mBeetrootCrop;
	static Block * mInfoReserved6;
	static Block * mNetherReactor;
	static Block * mStructureBlock; // 45581
	static Block * mInfoUpdateGame2;
	static Block * mLitRedStoneLamp;
	static Block * mWoodenDoorBirch;
	static Block * mDoubleWoodenSlab;
	static Block * mWoodenDoorAcacia;
	static Block * mWoodenDoorJungle;
	static Block * mWoodenDoorSpruce;
	static Block * mWoodenDoorDarkOak;
	static Block * mUnlitRedStoneTorch;
	static Block * mDaylightDetectorInverted;
	static Block * mIronDoor;
public:
	static float SIZE_OFFSET;
	static const char* BLOCK_DESCRIPTION_PREFIX;
};

//template function decompiled from libminecraftpe.so
template <typename BlockType,typename...Args>
BlockType& registerBlock(std::string const&name,int id,const Args&...rest)
{
	std::string const block_name = toLower(name);
	if(Block::mBlockLookupMap.count(block_name)!=0)
		return *(BlockType*)Block::mBlocks[id];
	
	BlockType* new_instance = new BlockType(name,id,rest...);
	Block::mBlocks[id] = new_instance;
	Block::mBlockLookupMap.emplace(block_name,(Block const*)new_instance);
	return *new_instance;
}
