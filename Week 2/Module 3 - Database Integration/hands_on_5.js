// ==============================
// TASK 1
// ==============================

// Create and switch to database
use("college_nosql");

// Create collection
db.createCollection("feedback");

// Insert the 10 feedback documents
db.feedback.insertMany([
  // Paste the same 10 documents here
]);

// Insert one document WITHOUT attachments

db.feedback.insertOne({
  student_id: 11,
  course_code: "CS103",
  semester: "2024-EVEN",
  rating: 4,
  comments: "Well-organized course with engaging lectures.",
  tags: ["organized", "interactive", "informative"],
  submitted_at: ISODate("2024-12-05T10:30:00Z")
});

// Verify insert

db.feedback.countDocuments();


// ==============================
// TASK 2 - CRUD
// ==============================

// 65
// Find all rating 5

db.feedback.find({
    rating:5
});

// 66
// CS101 with challenging tag

db.feedback.find({
    course_code:"CS101",
    tags:"challenging"
});

// 67
// Projection

db.feedback.find(
{},
{
    student_id:1,
    course_code:1,
    rating:1,
    _id:0
}
);

// 68
// Add needs_review

db.feedback.updateMany(
{
    rating:{
        $lt:3
    }
},
{
    $set:{
        needs_review:true
    }
}
);

// 69
// Push reviewed tag

db.feedback.updateMany(
{
    needs_review:true
},
{
    $push:{
        tags:"reviewed"
    }
}
);

// 70
// Delete semester

db.feedback.deleteMany({
    semester:"2021-EVEN"
});


// ==============================
// TASK 3 - Aggregation
// ==============================

// 71
// Average rating

db.feedback.aggregate([
{
    $match:{
        semester:"2022-ODD"
    }
},
{
    $group:{
        _id:"$course_code",
        avg_rating:{
            $avg:"$rating"
        },
        total_feedback:{
            $sum:1
        }
    }
},
{
    $sort:{
        avg_rating:-1
    }
}
]);


// 72
// Rename and round

db.feedback.aggregate([
{
    $match:{
        semester:"2022-ODD"
    }
},
{
    $group:{
        _id:"$course_code",
        avg_rating:{
            $avg:"$rating"
        },
        total_feedback:{
            $sum:1
        }
    }
},
{
    $project:{
        _id:0,
        course_code:"$_id",
        average_rating:{
            $round:["$avg_rating",1]
        },
        total_feedback:1
    }
},
{
    $sort:{
        average_rating:-1
    }
}
]);


// 73
// Tag frequency leaderboard

db.feedback.aggregate([
{
    $unwind:"$tags"
},
{
    $group:{
        _id:"$tags",
        count:{
            $sum:1
        }
    }
},
{
    $sort:{
        count:-1
    }
}
]);


// 74
// Create Index

db.feedback.createIndex({
    course_code:1
});

// Verify Index Usage

db.feedback.find({
    course_code:"CS101"
}).explain("executionStats");