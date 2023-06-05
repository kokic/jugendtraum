

def filterNotDir (entries : Array IO.FS.DirEntry) := 
  entries.filterM (·.path.isDir >>= (pure !·))

def writeFile path s :=
  IO.FS.Handle.mk path IO.FS.Mode.write >>= 
    λ file ↦ 
      bind (file.putStr s) λ _ ↦
      bind (file.flush) λ _ ↦
      pure ()


def listFile (path : String) := System.FilePath.readDir path
  >>= λ entries => bind (filterNotDir entries)
      λ filtered => pure (filtered.map (·.fileName))


-- item

def items := listFile "./images/items"

def assignItem (s : String) := 
  s!"{s.extract 0 ⟨s.length - 4⟩} = AssetsManager.get_items_path('{s}')\n"

def assignItems (xs : Array String) :=
  xs.map assignItem |>.foldl String.append 
"# item texture
empty = Texture(Image.new('RGBA', (16, 16), color=(0, 0, 0, 0)))
"

def writeItemsToFile := λ () ↦  
  items >>= λ xs ↦ xs 
    |> assignItems 
    |> writeFile "./.codegen/items.txt"
    |> pure



-- isotropic block

def isotropicBlocks := listFile "./images/blocks/isotropic"

def assignIsotropicBlock (s : String) := 
  s!"{s.extract 0 ⟨s.length - 4⟩} = AssetsManager.get_blocks_path('isotropic/{s}')\n"

def assignIsotropicBlocks (xs : Array String) :=
  xs.map assignIsotropicBlock |>.foldl String.append 
  "# isotropic block texture\n"


def writeIsotropicBlocksToFile := λ () ↦  
  isotropicBlocks >>= λ xs ↦ xs 
    |> assignIsotropicBlocks 
    |> writeFile "./.codegen/isotropic_blocks.txt"
    |> pure





-- register item 

def registerItem (s : String) :=
  let identifier := s.extract 0 ⟨s.length - 4⟩
  s!"Item.register_item('{identifier}', Item(Assets.{identifier}))\n"


def writeRegisterItemsToFile := λ () ↦  
  isotropicBlocks >>= λ xs ↦ xs 
    |>.map registerItem |>.foldl String.append ""
    |> writeFile "./.codegen/register_item.txt"
    |> pure



-- register block 

def registerIsotropicBlock (s : String) :=
  let identifier := s.extract 0 ⟨s.length - 4⟩
  s!"Block.register_block('{identifier}', IsotropicBlock(Assets.{identifier}))\n"


def writeIsotropicRegisterBlocksToFile := λ () ↦  
  isotropicBlocks >>= λ xs ↦ xs 
    |>.map registerIsotropicBlock |>.foldl String.append ""
    |> writeFile "./.codegen/register_isotropic_block.txt"
    |> pure





-- write


-- #eval writeItemsToFile ()
-- #eval writeIsotropicBlocksToFile ()
-- #eval writeRegisterItemsToFile ()
-- #eval writeIsotropicRegisterBlocksToFile ()
