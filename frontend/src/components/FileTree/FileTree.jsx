import { useState } from "react";

import "./FileTree.css";


function buildTree(files) {

    const root = {};

    files.forEach(file => {

        const parts = file.path.split("/");

        let current = root;


        parts.forEach((part, index) => {

            if (!current[part]) {

                current[part] = {

                    children: {},

                    isFile: index === parts.length - 1,

                    path: parts
                        .slice(0, index + 1)
                        .join("/")

                };

            }

            current = current[part].children;

        });

    });


    return root;

}



function TreeNode({

    name,
    node,
    onFileClick

}) {


    const [open, setOpen] = useState(false);


    if (node.isFile) {

        return (

            <div

                className="file-item"

                onClick={() =>
                    onFileClick(
                        {
                            file_path: node.path
                        },
                        null
                    )
                }

            >

                📄 {name}

            </div>

        );

    }


    return (

        <div className="folder">


            <div
                className="folder-item"
                onClick={() => setOpen(prev => !prev)}
            >

                {open ? "📂" : "📁"} {name}

            </div>


            {

                open && (

                    <div className="children">

                        {

                            Object.entries(node.children)

                            .map(([childName, childNode]) => (

                                <TreeNode

                                    key={childName}

                                    name={childName}

                                    node={childNode}

                                    onFileClick={onFileClick}

                                />

                            ))

                        }

                    </div>

                )

            }


        </div>

    );

}



function FileTree({

    files,

    onFileClick

}) {


    const tree = buildTree(files);


    return (

        <div className="file-tree">

            {

                Object.entries(tree)

                .map(([name, node]) => (

                    <TreeNode

                        key={name}

                        name={name}

                        node={node}

                        onFileClick={onFileClick}

                    />

                ))

            }

        </div>

    );

}


export default FileTree;