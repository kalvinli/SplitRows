from baseopensdk .api .base .v1 import *
from baseopensdk import BaseClient 
import os ,json ,re 
def split_text_func (OO0OO0O0OO00O00OO :str ,OOO0000OOOOO00O00 :str ,OOO0O00000O0OOOO0 :object ):
    OO0000O0O00OO000O =[]
    if OO0OO0O0OO00O00OO ==1 :
      O00000OO00O000OOO =[]
      for O0OO0O0OO0OO00000 in OOO0O00000O0OOOO0 :
        if O0OO0O0OO0OO00000 =='空格'or O0OO0O0OO0OO00000 =='space_symbol':
          O00000OO00O000OOO .append ("\ ")
        elif O0OO0O0OO0OO00000 =='换行符'or O0OO0O0OO0OO00000 =='newline_symbol':
          O00000OO00O000OOO .append ("\\n")
        elif O0OO0O0OO0OO00000 =='\\':
              O00000OO00O000OOO .append ("\\\\")
        elif O0OO0O0OO0OO00000 =='|'or O0OO0O0OO0OO00000 =='.'or O0OO0O0OO0OO00000 =='('or O0OO0O0OO0OO00000 ==')'or O0OO0O0OO0OO00000 =='['or O0OO0O0OO0OO00000 ==']'or O0OO0O0OO0OO00000 =='{'or O0OO0O0OO0OO00000 =='}'or O0OO0O0OO0OO00000 =='$'or O0OO0O0OO0OO00000 =='^'or O0OO0O0OO0OO00000 =='*'or O0OO0O0OO0OO00000 =='+'or O0OO0O0OO0OO00000 =='?':
              O00000OO00O000OOO .append ("\\"+O0OO0O0OO0OO00000 )
        else :
          O00000OO00O000OOO .append (O0OO0O0OO0OO00000 )
      O00O00O0O0OOOO0O0 ="|".join (O00000OO00O000OOO )
      OOOOO00O00O0O0OOO =re .split (O00O00O0O0OOOO0O0 ,OOO0000OOOOO00O00 )
      OO0000O0O00OO000O =[OOOO000O0OO0OOO0O for OOOO000O0OO0OOO0O in OOOOO00O00O0O0OOO if OOOO000O0OO0OOO0O is not None and OOOO000O0OO0OOO0O !='']
    elif OO0OO0O0OO00O00OO ==4 or OO0OO0O0OO00O00OO ==17 :
      for O0O00OO0OOO000O0O in OOO0000OOOOO00O00 :
        O0OOOO00O0000OOOO =[O0O00OO0OOO000O0O ]
        OO0000O0O00OO000O .append (O0OOOO00O0000OOOO )
    elif OO0OO0O0OO00O00OO ==11 :
      for O0O00OO0OOO000O0O in OOO0000OOOOO00O00 :
        O0OOOO00O0000OOOO =[{"id":O0O00OO0OOO000O0O .get ("id")}]
        OO0000O0O00OO000O .append (O0OOOO00O0000OOOO )
    elif OO0OO0O0OO00O00OO ==18 or OO0OO0O0OO00O00OO ==21 :
      OOO0000OOOOO00O00 =OOO0000OOOOO00O00 [0 ].get ("record_ids",[])
      for O0O00OO0OOO000O0O in OOO0000OOOOO00O00 :
        O0OOOO00O0000OOOO =[O0O00OO0OOO000O0O ]
        OO0000O0O00OO000O .append (O0OOOO00O0000OOOO )
    elif OO0OO0O0OO00O00OO ==19 or OO0OO0O0OO00O00OO ==20 :
      try :
        OOO0000OOOOO00O00 =OOO0000OOOOO00O00 [0 ].get ("text","")
        O00000OO00O000OOO =[]
        for O0OO0O0OO0OO00000 in OOO0O00000O0OOOO0 :
          if O0OO0O0OO0OO00000 =='空格'or O0OO0O0OO0OO00000 =='space_symbol':
            O00000OO00O000OOO .append ("\ ")
          elif O0OO0O0OO0OO00000 =='换行符'or O0OO0O0OO0OO00000 =='newline_symbol':
            O00000OO00O000OOO .append ("\\n")
          elif O0OO0O0OO0OO00000 =='\\':
                O00000OO00O000OOO .append ("\\\\")
          elif O0OO0O0OO0OO00000 =='|'or O0OO0O0OO0OO00000 =='.'or O0OO0O0OO0OO00000 =='('or O0OO0O0OO0OO00000 ==')'or O0OO0O0OO0OO00000 =='['or O0OO0O0OO0OO00000 ==']'or O0OO0O0OO0OO00000 =='{'or O0OO0O0OO0OO00000 =='}'or O0OO0O0OO0OO00000 =='$'or O0OO0O0OO0OO00000 =='^'or O0OO0O0OO0OO00000 =='*'or O0OO0O0OO0OO00000 =='+'or O0OO0O0OO0OO00000 =='?':
                O00000OO00O000OOO .append ("\\"+O0OO0O0OO0OO00000 )
          else :
            O00000OO00O000OOO .append (O0OO0O0OO0OO00000 )
        O00O00O0O0OOOO0O0 ="|".join (O00000OO00O000OOO )
        OOOOO00O00O0O0OOO =re .split (O00O00O0O0OOOO0O0 ,OOO0000OOOOO00O00 )
        OO0000O0O00OO000O =[O0O000O00O00OOOO0 for O0O000O00O00OOOO0 in OOOOO00O00O0O0OOO if O0O000O00O00OOOO0 is not None and O0O000O00O00OOOO0 !='']
      except Exception as OOO00000OO0O00O00 :
        OO0000O0O00OO000O =[]
    else :
      OO0000O0O00OO000O =OOO0000OOOOO00O00 
    return OO0000O0O00OO000O 
def batch_split_rows_func (OOOO0000OO0OO0O0O :str ):
  OOOO000OOO0OOO0OO =json .loads (OOOO0000OO0OO0O0O ).get ("parameters","")
  if OOOO000OOO0OOO0OO =='':
    return "参数错误"
  O0O000OOOO000OOO0 =OOOO000OOO0OOO0OO .get ("app_token")
  OOO0O0O00O0OO00OO =OOOO000OOO0OOO0OO .get ("personal_base_token")
  O0OOOO000OOO0OO00 =OOOO000OOO0OOO0OO .get ("table_id")
  O000000OO0000O0O0 =OOOO000OOO0OOO0OO .get ("view_id")
  OOOO0OOOO0OOO0000 =OOOO000OOO0OOO0OO .get ("field")
  OOOO000O00O0O0O0O =OOOO000OOO0OOO0OO .get ("field_type")
  O00O0OOOO000O0O0O =OOOO000OOO0OOO0OO .get ("field_sync")
  O0OOOOOOO00000OOO =OOOO000OOO0OOO0OO .get ("field_target")
  OO0OO00O0O0000O0O =OOOO000OOO0OOO0OO .get ("op_type")
  O0O00O0OOOOO00O00 =OOOO000OOO0OOO0OO .get ("field_father")
  OO000O0OOO0O0O000 =OOOO000OOO0OOO0OO .get ("delete_original_record")
  O0OOOO000O00O00O0 =OOOO000OOO0OOO0OO .get ("field_mapping")
  O0OO00O0OOOOOO000 =OOOO000OOO0OOO0OO .get ("separater")
  OOOOOOOOOO00OO0OO :BaseClient =BaseClient .builder ().app_token (O0O000OOOO000OOO0 ).personal_base_token (OOO0O0O00O0OO00OO ).build ()
  if OOOO000O00O0O0O0O ==19 or OOOO000O00O0O0O0O ==20 :
    if O0OOOOOOO00000OOO =="":
      try :
        O00O00OO00O0OO00O =CreateAppTableFieldRequest ().builder ().table_id (O0OOOO000OOO0OO00 ).request_body (AppTableField .builder ().field_name ("文本分行（自动添加）").type (1 ).build ()).build ()
        O00OOOOOO0O00000O =OOOOOOOOOO00OO0OO .base .v1 .app_table_field .create (O00O00OO00O0OO00O )
        O0OOOOOOO00000OOO ="文本分行（自动添加）"
      except Exception as O0O00OOO00O0O0O00 :
        O0OOOOOOO00000OOO ="文本分行（自动添加）"
  OOOOO00OO00OO0O00 =True 
  OO00OO000O0OO0O0O =""
  while OOOOO00OO00OO0O00 :
    O0O0O0O0OO0000O0O =ListAppTableRecordRequest .builder ().page_size (500 ).view_id (O000000OO0000O0O0 ).filter ("").table_id (O0OOOO000OOO0OO00 ).page_token (OO00OO000O0OO0O0O ).build ()
    O0OO000O00OO0000O =OOOOOOOOOO00OO0OO .base .v1 .app_table_record .list (O0O0O0O0OO0000O0O )
    OO0O000O00O000000 =getattr (O0OO000O00OO0000O .data ,'items',[])
    OOOOO00OO00OO0O00 =O0OO000O00OO0000O .data .has_more 
    OO00OO000O0OO0O0O =O0OO000O00OO0000O .data .page_token 
    OO0OO000O00000OO0 =O0OO000O00OO0000O .data .total 
    O0O000O0OO0OO0O00 ='成功拆分 '+str (OO0OO000O00000OO0 )+' 条数据'
    OOO0O0OOO00O0OO0O =[]
    O0OOOOOOOO0O0O000 =[]
    for OO0O0OOO00O00OO0O in OO0O000O00O000000 :
      OOO0O0OOO00O0OO0O .append (OO0O0OOO00O00OO0O .record_id )
      OOOO00O0000OOOO00 =OO0O0OOO00O00OO0O .fields 
      for OO0O0000OO00O0O0O ,O0OOO00O0000OO0O0 in OOOO00O0000OOOO00 .items ():
        OO000OO0O00O0OOO0 =[]
        if OO0O0000OO00O0O0O ==OOOO0OOOO0OOO0000 :
          OO000OO0O00O0OOO0 =split_text_func (OOOO000O00O0O0O0O ,O0OOO00O0000OO0O0 ,O0OO00O0OOOOOO000 )
          for OOOOO0O000O0O00OO in OO000OO0O00O0OOO0 :
            O00O000O000O0OOOO ={}
            if O0OOOOOOO00000OOO =="":
              O00O000O000O0OOOO [OOOO0OOOO0OOO0000 ]=OOOOO0O000O0O00OO 
            else :
              if OOOO000O00O0O0O0O ==19 or OOOO000O00O0O0O0O ==20 :
                O00O000O000O0OOOO [O0OOOOOOO00000OOO ]=OOOOO0O000O0O00OO 
              else :
                O00O000O000O0OOOO [OOOO0OOOO0OOO0000 ]=OOOOO0O000O0O00OO 
            if (OO0OO00O0O0000O0O =='子记录'or OO0OO00O0O0000O0O =='Child Records')and O0O00O0OOOOO00O00 !='':
              O00O000O000O0OOOO [O0O00O0OOOOO00O00 ]=[OO0O0OOO00O00OO0O .record_id ]
            if len (O00O0OOOO000O0O0O )!=0 :
              for OOO0OO0OO0O000O0O in O00O0OOOO000O0O0O :
                if O0OOOO000O00O00O0 =='{}':
                  O00O000O000O0OOOO [OOO0OO0OO0O000O0O ]=OOOO00O0000OOOO00 .get (OOO0OO0OO0O000O0O ,None )
                else :
                  O0OO0OOO0O000O0OO =json .loads (O0OOOO000O00O00O0 )
                  if O0OO0OOO0O000O0OO .get (OOO0OO0OO0O000O0O )is None :
                    O00O000O000O0OOOO [OOO0OO0OO0O000O0O ]=OOOO00O0000OOOO00 .get (OOO0OO0OO0O000O0O ,None )
                  else :
                    if OOOOO0O000O0O00OO ==O0OO0OOO0O000O0OO .get (OOO0OO0OO0O000O0O ):
                      O00O000O000O0OOOO [OOO0OO0OO0O000O0O ]=OOOO00O0000OOOO00 .get (OOO0OO0OO0O000O0O ,None )
                    else :
                      O00O000O000O0OOOO [OOO0OO0OO0O000O0O ]=None 
            O0OOOOOOOO0O0O000 .append ({"fields":O00O000O000O0OOOO })
    O0O000O0OO0OO0O00 =batch_create_record_func (O0O000OOOO000OOO0 ,OOO0O0O00O0OO00OO ,O0OOOO000OOO0OO00 ,O0OOOOOOOO0O0O000 )
    if len (OO000O0OOO0O0O000 )!=0 and (OO0OO00O0O0000O0O =='独立记录'or OO0OO00O0O0000O0O =='Independent Records'):
      O0O000O0OO0OO0O00 =batch_delete_record_func (O0O000OOOO000OOO0 ,OOO0O0O00O0OO00OO ,O0OOOO000OOO0OO00 ,OOO0O0OOO00O0OO0O )
  return O0O000O0OO0OO0O00 
def get_field_type_func (OOO0O0O0OO0OO0OOO :str ,O0O0OO0OO0OOO0OOO :str ,OO00O0O00OO0O0O00 :str ,OOO0OOOOOO00OOOO0 :str ,OOO0O00OOO000000O :str ):
  O00O0OO0O0O0OO000 :BaseClient =BaseClient .builder ().app_token (OOO0O0O0OO0OO0OOO ).personal_base_token (O0O0OO0OO0OOO0OOO ).build ()
  OOO0O0OOO00000OO0 =ListAppTableFieldRequest .builder ().page_size (300 ).table_id (OO00O0O00OO0O0O00 ).view_id (OOO0OOOOOO00OOOO0 ).build ()
  OOOOOOOOO0OO0O0O0 =O00O0OO0O0O0OO000 .base .v1 .app_table_field .list (OOO0O0OOO00000OO0 )
  O00OOOO0000O0OO00 =getattr (OOOOOOOOO0OO0O0O0 .data ,'items')or []
  OOOOO00000O00OOOO ="Text"
  for O0O0OOO00OOOOOO0O in O00OOOO0000O0OO00 :
    if OOO0O00OOO000000O ==O0O0OOO00OOOOOO0O .field_name :
      if O0O0OOO00OOOOOO0O .ui_type =='Text':
        OOOOO00000O00OOOO ="Text"
      elif O0O0OOO00OOOOOO0O .ui_type =='MultiSelect':
            OOOOO00000O00OOOO ="MultiSelect"
      elif O0O0OOO00OOOOOO0O .ui_type =='User':
        OOOOO00000O00OOOO ="User"
      elif O0O0OOO00OOOOOO0O .ui_type =='Lookup':
        OOOOO00000O00OOOO ="Lookup"
      elif O0O0OOO00OOOOOO0O .ui_type =='Formula':
        OOOOO00000O00OOOO ="Formula"
      else :
        OOOOO00000O00OOOO ="Text"
  return OOOOO00000O00OOOO 
def batch_create_record_func (O0000OO0OOO00OOO0 :str ,OOOOOOOOOO00OOO00 :str ,O0OO0OO000O0OOOOO :str ,OO0OO000O0OOOO0OO :object ):
  try :
    OOOO0OOO00O00O00O :BaseClient =BaseClient .builder ().app_token (O0000OO0OOO00OOO0 ).personal_base_token (OOOOOOOOOO00OOO00 ).build ()
    O00000OO000O00OOO =500 
    for OOOO0000OOO0O0OO0 in range (0 ,len (OO0OO000O0OOOO0OO ),O00000OO000O00OOO ):
      O0O0OOO00OO00OO00 =OO0OO000O0OOOO0OO [OOOO0000OOO0O0OO0 :OOOO0000OOO0O0OO0 +O00000OO000O00OOO ]
      O0000000000OO0000 =0 
      while O0000000000OO0000 <3 :
        try :
          O000OOOO00OOO00OO =BatchCreateAppTableRecordRequest ().builder ().table_id (O0OO0OO000O0OOOOO ).request_body (BatchCreateAppTableRecordRequestBody .builder ().records (O0O0OOO00OO00OO00 ).build ()).build ()
          O0OOO00000000O00O =OOOO0OOO00O00O00O .base .v1 .app_table_record .batch_update (O000OOOO00OOO00OO )
          O0000000000OO0000 =3 
          OO0OOOOOOO0O0O000 ="拆分数据保存成功"
        except Exception as O0O00000000OOOO0O :
          O0000000000OO0000 =O0000000000OO0000 +1 
          if O0000000000OO0000 ==3 :
            OO0OOOOOOO0O0O000 ="重试写入超过2次，数据操作失败，请检查网络！"
            raise "重试写入超过2次，数据操作失败，请检查网络！"
    return OO0OOOOOOO0O0O000 
  except Exception as O0O00000000OOOO0O :
    return "拆分数据保存失败"
def batch_delete_record_func (OOO0O0O00OOO0OOO0 :str ,O0OO00O00OO0O0OOO :str ,OO00000OO0O00OO00 :str ,OOOO0OO00OO0OOOO0 ):
  try :
    OO000OOOO0O00000O :BaseClient =BaseClient .builder ().app_token (OOO0O0O00OOO0OOO0 ).personal_base_token (O0OO00O00OO0O0OOO ).build ()
    OO00OOOO00O00OO00 =500 
    for OOOOO00OOO00O0O0O in range (0 ,len (OOOO0OO00OO0OOOO0 ),OO00OOOO00O00OO00 ):
      OO0OOOOO00O0O0OO0 =OOOO0OO00OO0OOOO0 [OOOOO00OOO00O0O0O :OOOOO00OOO00O0O0O +OO00OOOO00O00OO00 ]
      OO0O00O000OO0OOOO =0 
      while OO0O00O000OO0OOOO <3 :
        try :
          OOOOOO00OOO0OOOO0 =BatchDeleteAppTableRecordRequest ().builder ().app_token (OOO0O0O00OOO0OOO0 ).table_id (OO00000OO0O00OO00 ).request_body (BatchDeleteAppTableRecordRequestBody .builder ().records (OO0OOOOO00O0O0OO0 ).build ()).build ()
          OOOO000000OO0OOO0 =OO000OOOO0O00000O .base .v1 .app_table_record .batch_delete (OOOOOO00OOO0OOOO0 )
          OO0O00O000OO0OOOO =3 
          return "删除成功"
        except Exception as OOO000O000OO0OO0O :
          OO0O00O000OO0OOOO =OO0O00O000OO0OOOO +1 
          if OO0O00O000OO0OOOO ==3 :
            O000O0O0O00O0OOOO ="重试删除记录超过2次，数据操作失败，请检查网络！"
            raise "重试删除记录超过2次，数据操作失败，请检查网络！"
    return O000O0O0O00O0OOOO
  except Exception as OOO000O000OO0OO0O :
    return "删除失败"
