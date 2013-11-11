from sqlalchemy import Column, Integer, String
from oh_snap.database import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/guides.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import oh_snap.models
    Base.metadata.create_all(bind=engine)

#Eh, I'm done with this
class Guide(Base):
    __tablename__ = 'guides'

    id = Column(Integer, primary_keys=True)
    author = Column(String(50), unique=True)
    author_external_id = Column(String)
    author_image = Column(String)
    author_location_text = Column(String)
    author_profile = Column(String)
    author_tombstoned = Column(String)
    created = Column(Integer)
    guide_comment_count = Column(Integer)
    guide_id = Column(Integer)
    image = Column(String)
    is_hidden = Column(String)
    is_liked = Column(String)
    is_public = Column(String)
    like_count = Column(Integer)
    path = Column(String)
    primary_topic = Column(String)
    primary_topic_display_name = Column(String)
    public_snapshot_id = Column(Integer)
    short = Column(String)
    skip_popular_feed = Column(String)
    slug = Column(String)
    step_count = Column(Integer)
    summary = Column(String)
    supplies_comment_count = Column(Integer)
    title = Column(String)
    tombstoned = Column(String)
    topics = Column(String)
    total_comment_count = Column(Integer)
    uuid = Column(String)
    view_count = Column(Integer)

    def __init__(self, name=None, email=None):
        self.author = author

    def __repr__(self):
        return '<Author %r>' % (self.author)
